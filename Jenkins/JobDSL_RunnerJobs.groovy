job('Angular-Project-1-Runner') {
    scm {
        git('https://github.com/DipayanSinha/AngularProject-JobDSL.git', 'master')

    }
    triggers {
        scm('*/15****')
    }
    steps{
        batchFile('npm install')
        batchFile('npm install -g @angular/cli')
        batchFile('npm run ng build')
        powerShell('Compress-Archive -Path "C:\\Program Files (x86)\\Jenkins\\workspace\\DSL-Angular-Test\\dist\\*" -CompressionLevel Fastest -DestinationPath "C:\\Program Files (x86)\\Jenkins\\workspace\\DSL-Angular-Test\\dist.zip" -Force')
        powerShell('''$ADPass ="NphJpPEme="
            $ADPassword = $ADPass|ConvertTo-SecureString -AsPlainText -Force
            $credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList Administrator,$ADPassword
            $session = New-PSSession -ComputerName 52.43.216.143 -Credential $credential -Verbose
            Copy-Item -Path  "C:\\Program Files (x86)\\Jenkins\\workspace\\DSL-Angular-Test\\dist.zip\\*" -Destination C:\\inetpub\\wwwroot\\DSLProject -Recurse -ToSession $session -Verbose -Force''')
    }
}

