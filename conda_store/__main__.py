from conda_store import cli, logging


def main():
    logging.initialize_logging()
    cli.cli_conda_store()


if __name__ == "__main__":
    main()
