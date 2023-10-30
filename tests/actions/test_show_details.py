from pro_filer.actions.main_actions import show_details  # NOQA


def test_without_file(capsys):
    show_details({"base_path": "/home/trybe/blablabla"})
    expected = "File 'blablabla' does not exist\n"
    captured = capsys.readouterr()
    assert expected == captured.out


# Testar com algum arquivo válido
def test_with_valid_file(capsys):
    with open("Trybe_logo.png", "w"):
        pass
    show_details({"base_path": "Trybe_logo.png"})
    expected = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-10-30\n"
    )
    captured = capsys.readouterr()
    assert expected == captured.out


# Criar um arquivo sem extensão para testarß
def test_without_extension(capsys):
    show_details({"base_path": "pro_filer/actions/test_file"})
    expected = (
        "File name: test_file\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-10-30\n"
    )
    captured = capsys.readouterr()
    assert expected == captured.out
