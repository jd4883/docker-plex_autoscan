#!/usr/bin/env python3
import json
import os
from pathlib import Path


def set_value(environ, default):
	payload = default
	if environ in os.environ and os.environ[environ]:
		payload = os.environ[environ]
	return payload


if __name__ == "__main__":
	default_file_extensions = ["webm", "mkv", "flv", "vob", "ogv", "ogg", "drc", "gif", "gifv", "mng", "avi", "mov",
	                           "qt", "wmv", "yuv", "rm", "rmvb", "asf", "amv", "mp4", "m4p", "m4v", "mpg", "mp2",
	                           "mpeg", "mpe", "mpv", "m2v", "m4v", "svi", "3gp", "3g2", "mxf", "roq", "nsv", "f4v",
	                           "f4p", "f4a", "f4b", "mp3", "flac", "ts"]
	default_db_path = str("/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db")
	default_mime_types = list().append("video")
	default_plex_empty_trash_control_files = list().append("/mnt/unionfs/mounted.bin")
	default_plex_library_path = str("/usr/lib/plexmediaserver/lib")
	default_plex_local_url = str("http://localhost:32400")
	default_plex_scanner = "/usr/lib/plexmediaserver/Plex Media Scanner"
	default_plex_support_directory = "/var/lib/plexmediaserver/Library/Application Support"
	default_plex_user = str("plex")
	default_server_ignore_list = ["/.grab/", ".DS_Store", "Thumbs.db"]
	default_server_ip = str("0.0.0.0")
	default_server_pass = str("ChangeMe")
	default_server_scan_priorities = { "1": ["/Movies/"], "2": ["/TV/"] }
	
	config = dict()
	config["DOCKER_NAME"] = set_value("DOCKER_NAME", "plex")
	config["GOOGLE"] = dict()
	config["GOOGLE"]["ENABLED"] = set_value("GOOGLE_DRIVE_ENABLED", bool())
	config["GOOGLE"]["CLIENT_ID"] = set_value("GOOGLE_DRIVE_CLIENT_ID", str())
	config["GOOGLE"]["CLIENT_SECRET"] = set_value("GOOGLE_DRIVE_CLIENT_SECRET", str())
	config["GOOGLE"]["ALLOWED"] = dict()
	config["GOOGLE"]["ALLOWED"]["FILE_PATHS"] = set_value("GOOGLE_DRIVE_FILE_PATHS", list())
	config["GOOGLE"]["ALLOWED"]["FILE_EXTENSIONS"] = set_value("GOOGLE_DRIVE_FILE_EXTENSIONS", bool(True))
	config["GOOGLE"]["ALLOWED"]["FILE_EXTENSIONS_LIST"] = set_value("GOOGLE_DRIVE_FILE_EXTENSIONS_LIST",
	                                                                default_file_extensions)
	config["GOOGLE"]["ALLOWED"]["MIME_TYPES"] = set_value("GOOGLE_DRIVE_MIME_TYPES", bool(True))
	config["GOOGLE"]["ALLOWED"]["MIME_TYPES_LIST"] = set_value("GOOGLE_DRIVE_MIME_TYPES_LIST", default_mime_types)
	config["GOOGLE"]["TEAMDRIVE"] = set_value("GOOGLE_DRIVE_TEAMDRIVE", bool())
	config["GOOGLE"]["TEAMDRIVES"] = set_value("GOOGLE_DRIVE_TEAMDRIVES", list())
	config["GOOGLE"]["POLL_INTERVAL"] = set_value("GOOGLE_DRIVE_POLL_INTERVAL", 60)
	config["GOOGLE"]["SHOW_CACHE_LOGS"] = set_value("GOOGLE_DRIVE_SHOW_CACHE_LOGS", bool())
	config["PLEX_ANALYZE_DIRECTORY"] = set_value("PLEX_ANALYZE_DIRECTORY", bool(True))
	config["PLEX_ANALYZE_TYPE"] = set_value("PLEX_ANALYZE_TYPE", str("basic"))
	config["PLEX_FIX_MISMATCHED"] = set_value("PLEX_FIX_MISMATCHED", bool())
	config["PLEX_FIX_MISMATCHED_LANG"] = set_value("PLEX_FIX_MISMATCHED_LANG", str("en"))
	config["PLEX_DATABASE_PATH"] = set_value("PLEX_DATABASE_PATH", default_db_path)
	config["PLEX_EMPTY_TRASH"] = set_value("PLEX_EMPTY_TRASH", bool())
	config["PLEX_EMPTY_TRASH_CONTROL_FILES"] = set_value("PLEX_EMPTY_TRASH_CONTROL_FILES", bool())
	config["PLEX_EMPTY_TRASH_MAX_FILES"] = set_value("PLEX_EMPTY_TRASH_MAX_FILES", int(100))
	config["PLEX_EMPTY_TRASH_ZERO_DELETED"] = set_value("PLEX_EMPTY_TRASH_ZERO_DELETED", bool())
	config["PLEX_LD_LIBRARY_PATH"] = set_value("PLEX_LD_LIBRARY_PATH", default_plex_library_path)
	config["PLEX_SCANNER"] = set_value("PLEX_SCANNER", default_plex_scanner)
	config["PLEX_SUPPORT_DIR"] = set_value("PLEX_SUPPORT_DIR", default_plex_support_directory)
	config["PLEX_USER"] = set_value("PLEX_USER", default_plex_user)
	config["PLEX_TOKEN"] = set_value("PLEX_TOKEN", str())
	config["PLEX_LOCAL_URL"] = set_value("PLEX_LOCAL_URL", default_plex_local_url)
	config["PLEX_CHECK_BEFORE_SCAN"] = set_value("PLEX_CHECK_BEFORE_SCAN", bool())
	config["PLEX_WAIT_FOR_EXTERNAL_SCANNERS"] = set_value("PLEX_WAIT_FOR_EXTERNAL_SCANNERS", bool(True))
	config["RCLONE"] = dict()
	config["RCLONE"]["BINARY"] = set_value("RCLONE_BINARY", str())
	config["RCLONE"]["CONFIG"] = set_value("RCLONE_CONFIG", str())
	config["RCLONE"]["CRYPT_MAPPINGS"] = set_value("CRYPT_MAPPINGS", dict())
	config["RCLONE"]["RC_CACHE_REFRESH"] = dict()
	config["RCLONE"]["RC_CACHE_REFRESH"]["ENABLED"] = set_value("RCLONE_CACHE_REFRESH_ENABLED", bool())
	config["RCLONE"]["RC_CACHE_REFRESH"]["FILE_EXISTS_TO_REMOTE_MAPPINGS"] = set_value(
		"RCLONE_CACHE_REFRESH_FILE_EXISTS_TO_REMOTE_MAPPINGS", dict())
	# this should be a key value pair, with the value being provided as a list
	config["RCLONE"]["RC_URL"] = set_value("RCLONE_URL", str("http://localhost:5572"))
	config["RUN_COMMAND_BEFORE_SCAN"] = set_value("RUN_COMMAND_BEFORE_SCAN", str())
	config["RUN_COMMAND_AFTER_SCAN"] = set_value("RUN_COMMAND_AFTER_SCAN", str())
	config["SERVER_ALLOW_MANUAL_SCAN"] = set_value("RUN_COMMAND_AFTER_SCAN", bool())
	config["SERVER_FILE_EXIST_PATH_MAPPINGS"] = set_value("SERVER_FILE_EXIST_PATH_MAPPINGS", dict())
	# this should be a key value pair, with the value being provided as a list
	config["SERVER_IGNORE_LIST"] = set_value("SERVER_IGNORE_LIST", default_server_ignore_list)
	config["SERVER_IP"] = set_value("SERVER_IP", default_server_ip)
	config["SERVER_MAX_FILE_CHECKS"] = set_value("SERVER_MAX_FILE_CHECKS", int(10))
	config["SERVER_FILE_CHECK_DELAY"] = set_value("SERVER_FILE_CHECK_DELAY", int(60))
	config["SERVER_PASS"] = set_value("SERVER_PASS", default_server_pass)
	config["SERVER_PATH_MAPPINGS"] = set_value("SERVER_PATH_MAPPINGS", dict())
	config["SERVER_PORT"] = set_value("SERVER_PORT", int(3468))
	config["SERVER_SCAN_DELAY"] = set_value("SERVER_SCAN_DELAY", int(180))
	config["SERVER_SCAN_FOLDER_ON_FILE_EXISTS_EXHAUSTION"] = set_value("SERVER_SCAN_FOLDER_ON_FILE_EXISTS_EXHAUSTION",
	                                                                   bool())
	config["SERVER_SCAN_PRIORITIES"] = set_value("SERVER_SCAN_PRIORITIES", default_server_scan_priorities)
	config["SERVER_USE_SQLITE"] = set_value("SERVER_USE_SQLITE", bool(True))
	config["USE_DOCKER"] = set_value("USE_DOCKER", bool())
	config["USE_SUDO"] = set_value("USE_SUDO", bool())
	
	empty_keys = [k for k, v in config.items() if not v]
	for k in empty_keys:
		del config[k]
	
	base_plex_autoscan_config = set_value("PLEX_AUTOSCAN_CONFIG", str("config.json"))
	
	json.dump(config, open(Path(base_plex_autoscan_config), "w+"), indent = 4, sort_keys = True)
