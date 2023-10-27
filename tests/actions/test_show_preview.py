from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


# documentação:
# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#       ...
#     ],
# )
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py"
                ],
                "all_dirs": ["src", "src/utils"]
            },
            "Found 3 files and 2 directories\n"
            "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils"
            "/__init__.py']\nFirst 5 directories: ['src', 'src/utils']\n",
        ),
        (
            {
                "all_files": [
                        "file1.py",
                        "file2.py",
                        "file3.py",
                        "file4.py",
                        "file5.py",
                        "file6.py",
                    ],
                "all_dirs": ["dir1", "dir2"]
            },
            "Found 6 files and 2 directories\n"
            "First 5 files: ['file1.py', 'file2.py', 'file3.py', 'file4.py',"
            " 'file5.py']\nFirst 5 directories: ['dir1', 'dir2']\n",
        ),
        (
            {
                "all_files": [],
                "all_dirs": []
            },
            "Found 0 files and 0 directories\n",
        ),
    ],
)
def test_show_preview(test_input, expected, capsys):
    show_preview(test_input)
    captured = capsys.readouterr()
    assert expected == captured.out
