import pathway as pw


def build_live_table():
    docs = pw.io.fs.read(
        "data/tickets",
        format="plaintext_by_file",
    )

    return docs.select(
        content=pw.this.data
    )
