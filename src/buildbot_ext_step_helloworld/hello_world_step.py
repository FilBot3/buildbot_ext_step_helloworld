"""Buildbot Build Step Extension: HelloWorld
"""

# pylint: disable=import-error
from buildbot.process.buildstep import BuildStep
from buildbot.process.buildstep import ShellMixin
from twisted.internet import defer
# pylint: enable=import-error


class HelloWorld(ShellMixin, BuildStep):
    """HelloWorld BuildStep for a Buildbot Factory
    """
    name = 'helloworld'
    description = ['Print', 'Hello, World!', 'in', 'the', 'shell']

    def __init__(self, **kwargs):
        kwargs = self.setupShellMixin(kwargs)
        super().__init__(**kwargs)


    @defer.inlineCallbacks
    def run(self):
        """Main function called by BuildBot for BuildSteps
        """
        command = rm_command() # pylint: disable=undefined-variable
        self.setupLogfiles()
        cmd = yield self.makeRemoteShellCommand(command=command)
        yield self.runCommand(cmd)
        defer.returnValue(cmd.results())


    def rm_command() -> list:  # pylint: disable=no-method-argument
        """Returns the Hello World command as a list.
        """
        return ['echo', 'Hello, World!']
