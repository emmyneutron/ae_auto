from subprocess import Popen, PIPE


__author__ = 'Ahmed G. Ali'


def execute_command(cmd, user=None, interactive=False):
    """
    Executes shell command with the capability of specifying executing user.

    :param cmd: The command to be executed. could be more than one command separated by ``;``
    :type cmd: str
    :param user: Unix user used for execution.
    :type: str, None
    :param interactive: if `True`, command will be executed in interactive shell. i.e. using ``$bash -i -c``
    :return: std_out, std_err of execution output
    :rtype: :obj:`tuple` of :obj:`str`
    """
    _bash = '-c'
    if interactive:
        _bash = '-i -c'
    if user:
        cmd = """sudo -H -u %s bash %s "%s" """ % (user,_bash, cmd)
    # print 'executing: ', cmd

    p = Popen([cmd], stdout=PIPE, stderr=PIPE, shell=True)
    out, err = p.communicate()
    # print 'out: ', out
    # print 'err: ', err
    # print '=' *50
    # raw_input('Press any key to continue')
    return out, err


if __name__ == '__main__':
    out, err =  execute_command('ssh oy-ena-login-1 "cd /fire/staging/aexpress; ls E-MTAB-5481"', 'fg_cur',)
    for i in out.split('\n'):
        print i
    print '=' *50
    for i in err.split('\n'):
        print i
    print '=' *50
    # out, err =  execute_command('cd; pwd; ls -lah', 'gemmy',)
    # for i in out.split('\n'):
    #     print i