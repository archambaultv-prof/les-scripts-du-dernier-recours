###############################################################################
# c3hm : Corriger à 3 heures du matin
###############################################################################

import os
import subprocess

###############################################################################
# Helper functions
###############################################################################


def extract_student_info(folder_name: str) -> str:
    """
    Extract the student number and name from the folder name.

    The folder name should follow the Omnivox naming convention for students,
    which is:
    - One or more surname (letters ending with an underscore)
    - A digit only number ending with an underscore

    If the folder name does not match this pattern, return the empty string.
    """

    sub_parts = folder_name.split("_")
    student_info = []
    for part in sub_parts:
        if part.isdigit():
            student_info.append(part)
            return "_".join(student_info)
        else:
            student_info.append(part)
    # If we reach here, it means the folder name does not match the expected
    # pattern
    return ""


def is_student_folder(folder_name: str) -> bool:
    return extract_student_info(folder_name) != ""


def default_root_path() -> str:
    return os.getcwd()


def delete_item(candidate_path: str, dryrun: bool, verbose: bool) -> None:
    """
    Deletes the candidate_path using the appropriate native system command.

    If candidate_path is a directory:
        - Windows: uses "cmd /c rd /S /Q <candidate_path>"
        - Unix-like: uses "rm -rf <candidate_path>"
    If candidate_path is a file:
        - Windows: uses "cmd /c del /F /Q <candidate_path>"
        - Unix-like: uses "rm -f <candidate_path>"

    If dryrun is True, the action is logged but not executed.
    """
    # Determine if the candidate is a directory or a file.
    if os.path.isdir(candidate_path):
        if verbose:
            print(f"Removing {os.path.relpath(candidate_path)}")
        if not dryrun:
            if os.name == "nt":
                command = ["cmd", "/c", "rd", "/S", "/Q", candidate_path]
            else:
                command = ["rm", "-rf", candidate_path]
    elif os.path.isfile(candidate_path):
        if verbose:
            print(f"Removing {os.path.relpath(candidate_path)}")
        if not dryrun:
            if os.name == "nt":
                command = ["cmd", "/c", "del", "/F", "/Q", candidate_path]
            else:
                command = ["rm", "-f", candidate_path]
    else:
        if verbose:
            print(f"Skipping {os.path.relpath(candidate_path)} (not a file or directory)")
        return

    if not dryrun:
        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print(f"⚠️ Error removing {os.path.relpath(candidate_path)}")
            print("   Maybe a permission issue? Dare to use sudo? 😉")

###############################################################################
# poubelle command
###############################################################################


paths_to_delete = [
    "__pycache__",
    ".DS_Store",
    ".git",
    ".idea",
    ".pytest_cache",
    ".venv",
    "venv",
    ".vscode",
    "node_modules",
]


def remove_unwanted_dirs(root_path: str = None, verbose: bool = False,
                         dryrun: bool = False) -> None:
    """
    Recursively scans each student folder under root_path and deletes any file or directory
    whose name appears in the paths_to_delete set.

    Uses the delete_item() function for platform-dependent deletion commands.
    """
    if root_path is None:
        root_path = default_root_path()

    # Scan only directories in root_path that qualify as student folders.
    for item in os.listdir(root_path):
        student_folder_path = os.path.join(root_path, item)
        if os.path.isdir(student_folder_path) and is_student_folder(item):
            for current_root, dirs, files in os.walk(student_folder_path, topdown=True):
                # Process directories that match the deletion criteria.
                for d in list(dirs):
                    if d in paths_to_delete:
                        candidate_path = os.path.join(current_root, d)
                        delete_item(candidate_path, dryrun, verbose)
                        # Remove it from dirs to prevent os.walk from descending into it.
                        dirs.remove(d)
                # Process files that match the deletion criteria.
                for f in list(files):
                    if f in paths_to_delete:
                        candidate_file = os.path.join(current_root, f)
                        delete_item(candidate_file, dryrun, verbose)


def poubelle(root_path: str = None, verbose: bool = False,
             dryrun: bool = False) -> None:
    remove_unwanted_dirs(root_path, verbose, dryrun)


###############################################################################
# cli and main
###############################################################################


def build_parser():
    import argparse
    parser = argparse.ArgumentParser(
        description=("Nettoie les répertoires Omnivox avec panache !"
                     " Prépare-toi à un nettoyage intergalactique.")
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Sous-commande poubelle
    parser_poubelle = subparsers.add_parser("poubelle",
                                            help="Exécute la commande poubelle")
    parser_poubelle.add_argument(
        "root",
        nargs="?",
        default=None,
        help=("Chemin racine à nettoyer (par défaut, le repère des jedis : le répertoire courant).")
    )
    parser_poubelle.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Active le mode verbeux : des logs et des blagues de code en prime !"
    )
    parser_poubelle.add_argument(
        "--dryrun",
        action="store_true",
        help="Active le mode simulation (aucune action n'est réellement exécutée)."
    )
    parser_poubelle.set_defaults(func=do_poubelle)
    return parser


def do_poubelle(args):
    if args.dryrun:
        print("DRYRUN: Aucune action ne sera exécutée.")
        args.verbose = True
    poubelle(args.root, args.verbose, args.dryrun)


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
