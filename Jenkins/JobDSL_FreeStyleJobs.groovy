job('Angular-Runner-1') {
    scm {
        git {
            remote {
                url("https://github.com/DipayanSinha/AngularProject-JobDSL.git")
            }
            branch("master")
            configure { node ->
                node / 'extensions' / 'hudson.plugins.git.extensions.impl.SparseCheckoutPaths' / 'sparseCheckoutPaths' {
                    ['angular-1'].each { mypath ->
                        'hudson.plugins.git.extensions.impl.SparseCheckoutPath' {
                            path("${mypath}")
                        }
                    }
                }
                node / 'extensions' << 'hudson.plugins.git.extensions.impl.PathRestriction' {
                    includedRegions('angular-1/.*')
                    excludedRegions(['angular-2/.*\n','angular-3/.*\n','angular-4/.*\n','angular-5/.*\n'])
                }
            }
        }
    }
    triggers {
        scm('* * * * *')
    }
    publishers {
        downstream('Angular-Pipeline-1','SUCCESS')
    }
}
job('Angular-Runner-2') {
    scm {
        git {
            remote {
                url("https://github.com/DipayanSinha/AngularProject-JobDSL.git")
            }
            branch("master")
            configure { node ->
                node / 'extensions' / 'hudson.plugins.git.extensions.impl.SparseCheckoutPaths' / 'sparseCheckoutPaths' {
                    ['angular-2'].each { mypath ->
                        'hudson.plugins.git.extensions.impl.SparseCheckoutPath' {
                            path("${mypath}")
                        }
                    }
                }
                node / 'extensions' << 'hudson.plugins.git.extensions.impl.PathRestriction' {
                    includedRegions('angular-2/.*')
                    excludedRegions(['angular-1/.*\n','angular-3/.*\n','angular-4/.*\n','angular-5/.*\n'])
                }
            }
        }
    }
    triggers {
        scm('* * * * *')
    }
    publishers {
        downstream('Angular-Pipeline-2','SUCCESS')
    }
}
job('Angular-Runner-3') {
    scm {
        git {
            remote {
                url("https://github.com/DipayanSinha/AngularProject-JobDSL.git")
            }
            branch("master")
            configure { node ->
                node / 'extensions' / 'hudson.plugins.git.extensions.impl.SparseCheckoutPaths' / 'sparseCheckoutPaths' {
                    ['angular-3'].each { mypath ->
                        'hudson.plugins.git.extensions.impl.SparseCheckoutPath' {
                            path("${mypath}")
                        }
                    }
                }
                node / 'extensions' << 'hudson.plugins.git.extensions.impl.PathRestriction' {
                    includedRegions('angular3/.*')
                    excludedRegions(['angular-1/.*\n','angular-2/.*\n','angular-4/.*\n','angular-5/.*\n'])
                }
            }
        }
    }
    triggers {
        scm('* * * * *')
    }
    publishers {
        downstream('Angular-Pipeline-3','SUCCESS')
    }
}
job('Angular-Runner-4') {
    scm {
        git {
            remote {
                url("https://github.com/DipayanSinha/AngularProject-JobDSL.git")
            }
            branch("master")
            configure { node ->
                node / 'extensions' / 'hudson.plugins.git.extensions.impl.SparseCheckoutPaths' / 'sparseCheckoutPaths' {
                    ['angular-4'].each { mypath ->
                        'hudson.plugins.git.extensions.impl.SparseCheckoutPath' {
                            path("${mypath}")
                        }
                    }
                }
                node / 'extensions' << 'hudson.plugins.git.extensions.impl.PathRestriction' {
                    includedRegions('angular-4/.*')
                    excludedRegions(['angular-1/.*\n','angular-2/.*\n','angular-3/.*\n','angular-5/.*\n'])
                }
            }
        }
    }
    triggers {
        scm('* * * * *')
    }
    publishers {
        downstream('Angular-Pipeline-4','SUCCESS')
    }
}
job('Angular-Runner-5') {
    scm {
        git {
            remote {
                url("https://github.com/DipayanSinha/AngularProject-JobDSL.git")
            }
            branch("master")
            configure { node ->
                node / 'extensions' / 'hudson.plugins.git.extensions.impl.SparseCheckoutPaths' / 'sparseCheckoutPaths' {
                    ['angular-5'].each { mypath ->
                        'hudson.plugins.git.extensions.impl.SparseCheckoutPath' {
                            path("${mypath}")
                        }
                    }
                }
                node / 'extensions' << 'hudson.plugins.git.extensions.impl.PathRestriction' {
                    includedRegions('angular-5/.*')
                    excludedRegions(['angular-1/.*\n','angular-2/.*\n','angular-3/.*\n','angular-4/.*\n'])
                }
            }
        }
    }
    triggers {
        scm('* * * * *')
    }
    publishers {
        downstream('Angular-Pipeline-5','SUCCESS')
    }
}

