#!/usr/bin/env python3
import http.server
import socketserver
import os
import hashlib

PORT = 8080
DIRECTORY = "/home/user/BrickPoint"

def get_file_info(filename):
    path = os.path.join(DIRECTORY, filename)
    if not os.path.exists(path):
        return None
    size_bytes = os.path.getsize(path)
    size_kb = size_bytes / 1024
    with open(path, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()
    return {
        "name": filename,
        "size_kb": f"{size_kb:.1f} KB",
        "size_bytes": size_bytes,
        "sha256": sha256
    }

class DownloadHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_HEAD(self):
        if self.path in ['/', '/index.html']:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return
        if self.path.endswith('.zip'):
            filename = os.path.basename(self.path.split('?')[0])
            filepath = os.path.join(DIRECTORY, filename)
            if os.path.exists(filepath):
                filesize = os.path.getsize(filepath)
                self.send_response(200)
                self.send_header("Content-Type", "application/zip")
                self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
                self.send_header("Content-Length", str(filesize))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                return
        super().do_HEAD()

    def do_GET(self):
        # Allow CORS
        if self.path in ['/', '/index.html']:
            v2_info = get_file_info("brickpoint-wordpress-elementor-final-v2.zip")
            v1_info = get_file_info("brickpoint-wordpress-elementor-final.zip")
            
            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BrickPoint Theme Download Portal</title>
  <style>
    :root {{
      --primary: #c2410c;
      --primary-hover: #9a3412;
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --border: #334155;
      --accent: #22c55e;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 40px 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
    }}
    .container {{
      max-width: 800px;
      width: 100%;
    }}
    header {{
      text-align: center;
      margin-bottom: 40px;
    }}
    .badge {{
      display: inline-block;
      padding: 6px 14px;
      background: rgba(194, 65, 12, 0.2);
      border: 1px solid var(--primary);
      color: #fb923c;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
    }}
    h1 {{
      font-size: 2.4rem;
      font-weight: 800;
      margin-bottom: 12px;
      background: linear-gradient(135deg, #fff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    p.lead {{
      font-size: 1.1rem;
      color: var(--text-muted);
      max-width: 600px;
      margin: 0 auto;
    }}
    .download-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 32px;
      margin-bottom: 24px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
      position: relative;
      overflow: hidden;
    }}
    .download-card.featured {{
      border-color: var(--primary);
      box-shadow: 0 0 30px rgba(194, 65, 12, 0.15);
    }}
    .card-ribbon {{
      position: absolute;
      top: 18px;
      right: 20px;
      background: var(--accent);
      color: #000;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      text-transform: uppercase;
    }}
    .card-title {{
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .card-desc {{
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-bottom: 20px;
    }}
    .meta-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      background: rgba(15, 23, 42, 0.6);
      padding: 16px;
      border-radius: 8px;
      margin-bottom: 24px;
      font-size: 0.9rem;
    }}
    .meta-item strong {{
      display: block;
      color: var(--text-muted);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 2px;
    }}
    .checksum {{
      font-family: monospace;
      font-size: 0.75rem;
      color: #a5b4fc;
      word-break: break-all;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      background: var(--primary);
      color: #fff;
      font-size: 1.05rem;
      font-weight: 600;
      padding: 14px 24px;
      border-radius: 10px;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .btn:hover {{
      background: var(--primary-hover);
      transform: translateY(-1px);
    }}
    .btn-secondary {{
      background: #334155;
    }}
    .btn-secondary:hover {{
      background: #475569;
    }}
    .instructions {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
    }}
    .instructions h3 {{
      font-size: 1.1rem;
      margin-bottom: 12px;
    }}
    .instructions ol {{
      padding-left: 20px;
      color: var(--text-muted);
      font-size: 0.9rem;
    }}
    .instructions li {{
      margin-bottom: 8px;
    }}
    .instructions li strong {{
      color: var(--text);
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badge">Official WordPress Theme Release</div>
      <h1>BrickPoint Theme Direct Download</h1>
      <p class="lead">Production-ready WordPress theme package converted from Next.js with true granular Elementor Free & Pro editability.</p>
    </header>

    <!-- Main Deliverable v2 -->
    <div class="download-card featured">
      <div class="card-ribbon">Recommended v2</div>
      <div class="card-title">BrickPoint Elementor Final v2</div>
      <div class="card-desc">Contains granular Elementor sections, zero black-box monolithic widgets, Elementor Pro Theme Builder header/footer, and automated demo import data.</div>
      
      <div class="meta-grid">
        <div class="meta-item">
          <strong>Filename</strong>
          <span>brickpoint-wordpress-elementor-final-v2.zip</span>
        </div>
        <div class="meta-item">
          <strong>File Size</strong>
          <span>{v2_info['size_kb'] if v2_info else 'N/A'}</span>
        </div>
        <div class="meta-item" style="grid-column: 1 / -1;">
          <strong>SHA-256 Checksum</strong>
          <span class="checksum">{v2_info['sha256'] if v2_info else 'N/A'}</span>
        </div>
      </div>

      <a href="/brickpoint-wordpress-elementor-final-v2.zip" class="btn" download>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        Download Theme ZIP (v2 - Direct Link)
      </a>
    </div>

    <!-- Legacy Package v1 -->
    <div class="download-card">
      <div class="card-title">BrickPoint Elementor Final v1</div>
      <div class="card-desc">Theme package with Elementor template kits and initial custom widget configuration.</div>
      
      <div class="meta-grid">
        <div class="meta-item">
          <strong>Filename</strong>
          <span>brickpoint-wordpress-elementor-final.zip</span>
        </div>
        <div class="meta-item">
          <strong>File Size</strong>
          <span>{v1_info['size_kb'] if v1_info else 'N/A'}</span>
        </div>
      </div>

      <a href="/brickpoint-wordpress-elementor-final.zip" class="btn btn-secondary" download>
        Download Theme ZIP (v1)
      </a>
    </div>

    <!-- Instructions -->
    <div class="instructions">
      <h3>Quick Installation Guide</h3>
      <ol>
        <li>Download <strong>brickpoint-wordpress-elementor-final-v2.zip</strong> above.</li>
        <li>In WordPress Admin, go to <strong>Appearance &rarr; Themes &rarr; Add New &rarr; Upload Theme</strong>.</li>
        <li>Select the downloaded ZIP file and click <strong>Install Now</strong>, then click <strong>Activate</strong>.</li>
        <li>Ensure <strong>Elementor</strong> (Free or Pro) is installed and active.</li>
        <li>Go to <strong>Appearance &rarr; BrickPoint Demo</strong> and click <strong>Import Demo Content</strong>.</li>
        <li>All pages are automatically populated with native Elementor sections ready to be edited with <em>Edit with Elementor</em>!</li>
      </ol>
    </div>
  </div>
</body>
</html>
"""
            encoded = html.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(encoded)
            return

        # For zip file downloads
        if self.path.endswith('.zip'):
            filename = os.path.basename(self.path.split('?')[0])
            filepath = os.path.join(DIRECTORY, filename)
            if os.path.exists(filepath):
                filesize = os.path.getsize(filepath)
                self.send_response(200)
                self.send_header("Content-Type", "application/zip")
                self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
                self.send_header("Content-Length", str(filesize))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                with open(filepath, 'rb') as f:
                    while chunk := f.read(65536):
                        self.wfile.write(chunk)
                return

        super().do_GET()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), DownloadHandler) as httpd:
        print(f"Download server running at http://0.0.0.0:{PORT}/")
        httpd.serve_forever()
