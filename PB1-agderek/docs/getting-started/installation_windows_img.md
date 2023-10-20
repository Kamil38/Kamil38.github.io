# Installatie Windows

Voor de installatie in Windows raden we sterk aan om een aantal extra opties tijdens het installeren te selecteren.

1. Installeer Python.
    1. Zet een vinkje bij "Add python.exe to PATH"<br>![](img/python_installer_path.png)
    2. Kies de Disable path length limit optie<br>![](img/python_installed_disable_path_length.png)
2. Installeer VSCode.
    1. Puur optioneel maar handig om de context menu opties aan te vinken.<br>![](img/vscode_installer_context_menu.png)
    2. Vink Launch VScode uit. We starten de applicatie pas later.<br>![](img/vscode_installer_dont_launch.png)
3. Installeer Git.
    1. Zet main als default branch.<br>![](img/git_installer_main_branch.png)
    2. Zet VScode als default editor.<br>![](img/git_installer_editor.png)
    3. Kies de external OpenSSH.<br>![](img/git_installer_ssh.png)
4. Installeer Docker
    1. Het kan zijn dat je eerst nog virtualization in de bios moet aanzetten. Vraag eventueel studentmentor of docent om hulp. 
    2. Standaard opties, herstart de computer als gevraagd.
    3. Je krijgt na het herstarten van de computer mogelijk de volgende foutmelding:<br>![](img/docker_wsl_error.png)<br>Start powershell en voer het commando uit zoals aangegeven in de foutmelding:
    ```wsl --update```