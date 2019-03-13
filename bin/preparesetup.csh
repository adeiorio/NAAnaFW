cmsenv
setenv XRD_NETWORKSTACK IPv4
voms-proxy-init --voms cms --valid 192:00
set FILECERT="x509up_u`id -u`"
echo $FILECERT
cp /tmp/$FILECERT $HOME
setenv X509_USER_PROXY $HOME/$FILECERT
echo $X509_USER_PROXY
