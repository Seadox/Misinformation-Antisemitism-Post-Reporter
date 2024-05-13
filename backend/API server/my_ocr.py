import easyocr


class MyOCR:

    def get_text(image_path):
        reader = easyocr.Reader(
            ['en'], gpu=True, verbose=False, detector='dbnet18')
        result = reader.readtext(image_path, detail=0,
                                 paragraph=True, batch_size=5)

        return "".join(result)
