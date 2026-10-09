#!/usr/bin/env python3
"""
Lottie & dotLottie Automation Manager (Vibes Ecosystem)
CLI utility to search, download, inspect, and optimize Lottie animations.
"""

import sys
import os
import json
import urllib.request
import urllib.parse
import argparse

def search_lottie(query, limit=10):
    """Search public Lottie animations via LottieFiles endpoint."""
    encoded = urllib.parse.quote(query)
    url = f"https://lottiefiles.com/api/search/get-animations?query={encoded}&limit={limit}&format=json"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", {}).get("data", data)
    except Exception as e:
        return {"error": str(e)}

def inspect_lottie(file_path):
    """Read Lottie JSON and report technical metadata."""
    if not os.path.exists(file_path):
        print(f"Error: file not found: {file_path}")
        return None
    
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            d = json.load(f)
        except Exception as e:
            print(f"Invalid JSON: {e}")
            return None
    
    fps = d.get("fr", 30)
    in_point = d.get("ip", 0)
    out_point = d.get("op", 60)
    frames = out_point - in_point
    duration_sec = frames / fps if fps else 0
    w = d.get("w", 0)
    h = d.get("h", 0)
    v = d.get("v", "unknown")
    layers_count = len(d.get("layers", []))
    assets_count = len(d.get("assets", []))
    
    meta = {
        "version": v,
        "width": w,
        "height": h,
        "fps": fps,
        "total_frames": frames,
        "duration_seconds": round(duration_sec, 2),
        "layers": layers_count,
        "assets": assets_count,
        "file_size_kb": round(os.path.getsize(file_path) / 1024, 1)
    }
    return meta

def optimize_lottie(src_path, dst_path=None):
    """Strip unused metadata and minify JSON to minimize payload."""
    if not dst_path:
        dst_path = src_path.replace(".json", ".min.json")
    
    with open(src_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    
    # Strip unnecessary editor keys
    keys_to_clean = ["markers", "chars", "meta", "generator"]
    for k in keys_to_clean:
        if k in d and not d[k]:
            del d[k]
            
    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump(d, f, separators=(',', ':'))
        
    orig_size = os.path.getsize(src_path) / 1024
    new_size = os.path.getsize(dst_path) / 1024
    saved = ((orig_size - new_size) / orig_size) * 100 if orig_size else 0
    print(f"Optimized: {src_path} ({orig_size:.1f} KB) -> {dst_path} ({new_size:.1f} KB, -{saved:.1f}%)")

def main():
    parser = argparse.ArgumentParser(description="Lottie Manager for Vibes Engine")
    sub = parser.add_subparsers(dest="cmd")
    
    # inspect
    p_ins = sub.add_parser("inspect", help="Inspect Lottie JSON metadata")
    p_ins.add_argument("file", help="Path to .json Lottie file")
    
    # optimize
    p_opt = sub.add_parser("optimize", help="Minify and clean Lottie JSON")
    p_opt.add_argument("file", help="Source .json Lottie file")
    p_opt.add_argument("-o", "--output", help="Destination file path")
    
    # search
    p_srch = sub.add_parser("search", help="Search public Lottie animations")
    p_srch.add_argument("query", help="Search query (e.g. checkmark, loader)")
    p_srch.add_argument("-n", "--limit", type=int, default=5, help="Result limit")

    args = parser.parse_args()
    if args.cmd == "inspect":
        res = inspect_lottie(args.file)
        if res:
            print(json.dumps(res, indent=2))
    elif args.cmd == "optimize":
        optimize_lottie(args.file, args.output)
    elif args.cmd == "search":
        res = search_lottie(args.query, args.limit)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
