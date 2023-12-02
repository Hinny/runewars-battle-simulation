import logging

def setup_loggers():

    # Creating loggers
    detailed_logger = logging.getLogger('detailed_battle_logger')
    summary_logger = logging.getLogger('summary_battle_logger')

    # Set the logger level to the lowest desired level
    detailed_logger.setLevel(logging.DEBUG)
    summary_logger.setLevel(logging.DEBUG)

    # Adding console handler for detailed_logger if not already present
    if not any(isinstance(handler, logging.StreamHandler) for handler in detailed_logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_formatter)
        detailed_logger.addHandler(console_handler)

    # Checking if detailed_logger already has a FileHandler
    if not any(isinstance(handler, logging.FileHandler) for handler in detailed_logger.handlers):
        # Adding file handler for detailed_logger with timestamp
        detailed_file_handler = logging.FileHandler('detailed_battle.log')
        detailed_file_handler.setLevel(logging.INFO)
        detailed_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        detailed_file_handler.setFormatter(detailed_formatter)
        detailed_logger.addHandler(detailed_file_handler)

    # Performing the same check for summary_logger
    if not any(isinstance(handler, logging.FileHandler) for handler in summary_logger.handlers):
        # Adding file handler for summary_logger with timestamp
        summary_file_handler = logging.FileHandler('summary_battle.log')
        summary_file_handler.setLevel(logging.DEBUG)
        summary_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        summary_file_handler.setFormatter(summary_formatter)
        summary_logger.addHandler(summary_file_handler)

    return detailed_logger, summary_logger
