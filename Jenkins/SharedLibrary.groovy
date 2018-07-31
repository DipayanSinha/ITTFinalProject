
@Library('SharedLibraryJenkins')_

stage('Demo') {
    echo 'Hello world'
    SayHello('Jenkins')
}