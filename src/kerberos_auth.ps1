$kerberosTicket = klist tgt
if ($kerberosTicket) {
    Write-Host "Kerberos authentication successful"
} else {
    Write-Host "Kerberos authentication failed"
}
