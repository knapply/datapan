Set-PSDebug -trace 2

function Invoke-Call
{
    param ([scriptblock]$ScriptBlock)
    & @ScriptBlock
    if ($LastExitCode -ne 0)
    {
        exit $LastExitCode
    }
}

Invoke-Call { tox -c "tox.ini" -e py }
