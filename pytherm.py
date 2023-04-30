from escpos.printer import File as _Fl

class thermal:
    def __init__(self, device="/dev/usb/lp0"):
        self._device = _Fl(device)
        self.left()
        self.regular()

    def cut(self, lines=3):
        self._device.cut()

    def line(self, count=1):
        self._device.text("\n" * count)

    def write(self, data="", end="\n"):
        if self._device is not None:
            self._device.text(data + end)

    def cat(self, filename):
        if self._device is not None:
            with open(filename, "r") as f:
                data = f.read()
                self.write(data, end="")


    def left(self):
        self._device.text("\x1b\x61\x00")

    def center(self):
        self._device.text("\x1b\x61\x01")

    def right(self):
        self._device.text("\x1b\x61\x02")

    def bold(self):
        self._device.text("\x1b\x21\x08")

    def regular(self):
        self._device.text("\x1b\x21\x00")

    def qr(self, content, ec=2, size=10):
        self._device.qr(content, ec, size)

    def image(self, path):
        self._device.image(path)


