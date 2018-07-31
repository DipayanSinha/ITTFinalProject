node {
    try{
        stage('checkout')
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'SparseCheckoutPaths', sparseCheckoutPaths: [[path: 'angular-1']]]], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/DipayanSinha/AngularProject-JobDSL']]])
        stage 'build'
        bat '''cd "angular-1"
            npm install'''
        bat '''cd "angular-1"
            npm install -g @angular/cli'''
        bat '''cd "angular-1"
            npm run ng build'''

        stage 'deploy build to EC2'

        powershell 'Compress-Archive -Path "C:\\Program Files (x86)\\Jenkins\\workspace\\DSL-Jobs-Angular\\Angular-Pipeline-1\\angular-1\\dist\\*" -CompressionLevel Fastest -DestinationPath "C:\\Program Files (x86)\\Jenkins\\workspace\\DSL-Jobs-Angular\\Angular-Pipeline-1\\angular-1\\dist.zip" -Force'
        powershell '''$ADPass ="NphJpPEme="
            $ADPassword = $ADPass|ConvertTo-SecureString -AsPlainText -Force
            $credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList Administrator,$ADPassword
            $session = New-PSSession -ComputerName 54.71.241.91 -Credential $credential -Verbose
            Copy-Item -Path  "C:\\Program Files (x86)\\Jenkins\\workspace\\DSL-Jobs-Angular\\Angular-Pipeline-1\\angular-1\\dist.zip" -Destination "C:\\inetpub\\wwwroot\\AngularProjectsDSL\\Angular-1" -Recurse -ToSession $session -Verbose -Force'''

        stage 'email success'
        emailext body: 'Successfully Deployed', subject: 'Build Success - Angular Project 1', to: 'dipayan.sinha@intimetec.com'
    }catch(Exception e){
        stage 'email failure'
        emailext body: "${e}", subject: 'Build Failure - Angular Project 1', to: 'dipayan.sinha@intimetec.com'
    }
}


