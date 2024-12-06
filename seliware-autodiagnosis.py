from pyuac import main_requires_admin
import colorama, os

@main_requires_admin
def main():
	print(f"{colorama.Fore.CYAN} [+] Escalation successful! {colorama.Style.RESET_ALL}")
	print(f"{colorama.Fore.GREEN} [?] Running Seliware auto-diagnosis... {colorama.Style.RESET_ALL}")

	# Reset registry entry
	os.system(r'reg add "HKLM\SOFTWARE\Seliware" /v Version /t REG_SZ /d 0 /f')
	print(f"{colorama.Fore.GREEN} [+] Registry reset! {colorama.Style.RESET_ALL}")

	# Delete installation
	appdata_path = os.getenv("APPDATA")
	seliware_path = os.path.join(appdata_path, "Seliware")

	if os.path.exists(seliware_path):
		os.system(f"rmdir /s /q {seliware_path}")
	
	# Check if the installation still exists, if it does there must be a lock on one of the files.
	# We need to find the processes locking it and kill it.

	if os.path.exists(seliware_path):
		print(f"{colorama.Fore.RED} [!] Unable to delete Seliware installation! File may be locked. {colorama.Style.RESET_ALL}")
		print(f"{colorama.Fore.GREEN} [?] Attempting to kill processes locking the installation... {colorama.Style.RESET_ALL}")

		os.system('taskkill /f /im "ExploitUI.exe"')
		os.system('taskkill /f /im "Seliware.exe"')
		os.system('taskkill /f /im "SeliwareLoaderRewrite.exe"')
	
		os.system(f"rmdir /s /q {seliware_path}")

		if os.path.exists(seliware_path):
			print(f"{colorama.Fore.RED} [!] Unable to delete Seliware installation! {colorama.Style.RESET_ALL}")
			print(f"{colorama.Fore.GREEN} [?] Please manually delete the installation at {seliware_path} {colorama.Style.RESET_ALL}")
		else:
			print(f"{colorama.Fore.GREEN} [+] File unlocked & Seliware installation deleted! {colorama.Style.RESET_ALL}")
	else:
		print(f"{colorama.Fore.GREEN} [+] Seliware installation deleted! {colorama.Style.RESET_ALL}")

	# Also, we delete SeliwareBinaries.zip and SeliwareCef.zip in Appdata/Local/Temp if they exist.
	temp_path = os.getenv("TEMP")
	seliware_binaries_zip = os.path.join(temp_path, "SeliwareBinaries.zip")
	seliware_cef_zip = os.path.join(temp_path, "SeliwareCef.zip")

	if os.path.exists(seliware_binaries_zip):
		os.remove(seliware_binaries_zip)
		print(f"{colorama.Fore.GREEN} [+] Deleted SeliwareBinaries.zip {colorama.Style.RESET_ALL}")

	if os.path.exists(seliware_cef_zip):
		os.remove(seliware_cef_zip)
		print(f"{colorama.Fore.GREEN} [+] Deleted SeliwareCef.zip {colorama.Style.RESET_ALL}")

	print(f"{colorama.Fore.GREEN} [+] Reset all Seliware installation data. {colorama.Style.RESET_ALL}")

	# Well, we tried our best.
	print(f"{colorama.Fore.GREEN} [+] Seliware auto-diagnosis complete! Try re-running the installer! {colorama.Style.RESET_ALL}")

if __name__ == "__main__":
	main()