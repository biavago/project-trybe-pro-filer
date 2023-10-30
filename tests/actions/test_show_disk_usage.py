from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import unittest.mock


def test_with_empty_file(capsys):
    show_disk_usage({"all_files": []})
    expected = "Total size: 0\n"
    captured = capsys.readouterr()
    assert expected == captured.out


def test_with_all_files(capsys, tmp_path):
    path_1 = tmp_path / "tmp_path_1.txt"
    path_1.write_text("xxxx")

    path_2 = tmp_path / "tmp_path_2.txt"
    path_2.write_text("xxxxxxxx")

    mock_file = unittest.mock.Mock(return_value="/xxxxxx/")

    context = {
        "all_files": [
            f"{path_1}",
            f"{path_2}"
        ]
    }

    expected = (
        "'/xxxxxx/':                                             "
        "               8 (66%)\n'/xxxxxx/':                      "
        "                                      4 (33%)\nTotal size: 12\n"
    )

    with unittest.mock.patch(
        "pro_filer.actions.main_actions._get_printable_file_path",
        mock_file,
    ):
        show_disk_usage(context)
        captured = capsys.readouterr()
        assert expected == captured.out
