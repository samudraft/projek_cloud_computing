from http.server import
BaseHTTPRequestHandler
from PIL import Image, ImageOps
import io

class handler(BaseHTTPRequestHandler):
  def do_POST(self):
    # Membaca data gambar yang dikirim user
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)

    # Proses pengolahan gambar(contohnya grayscale)
    img = Image.open(io.BytesIO(post_data))
    img_gray = ImageOps.grayscale(img)

    # Simpan hasil ke memori (buffer)
    buffer = io.BytesIO()
    img_gray.save(buffer, format="JPEG")

    # Kirim balik ke user
    self.send_response(200)
    self.send_header('Content-type','image/jpeg')
    self.end_headers()

    self.wfile.write(buffer.getvalue())
