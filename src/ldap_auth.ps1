$ldapServer = "ldap://your-ldap-server"
$ldapUsername = "CN=Administrator,CN=Users,DC=example,DC=com"
$ldapPassword = "your-password"

$ldapConnection = New-Object DirectoryServices.DirectorySearcher($ldapServer, $ldapUsername, $ldapPassword)
$ldapConnection.SearchScope = [System.DirectoryServices.SearchScope]::Subtree
$ldapConnection.Filter = "(uid=username)"
$result = $ldapConnection.FindOne()

if ($result) {
    Write-Host "User found: $($result.Properties['uid'])"
} else {
    Write-Host "User not found"
}
