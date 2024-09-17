from audioop import reverse
from os import chdir
from pathlib import Path


def sort_files(path: Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {
            Path('video'): ['avi', 'mkv'],
            Path('image'): ['jpg', 'png'],
            Path('audio'): ['mp3', 'wav', 'ogg']
        }

    print(groups)
    reverse_groups = dict()
    for target_dir, extension_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        # print(target_dir, extension_list)
        for ext in extension_list:
            reverse_groups[f'.{ext}'] = target_dir
    print(reverse_groups)

    for file in path.iterdir():
        # print([file])
        # print(file.suffix)
        # print(file.name)
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    sort_files(Path(r'D:\Python projects\Advanced_python_course\Seminar_7\test_dir_for_task6'))
