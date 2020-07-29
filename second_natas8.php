#!/usr/bin/php7.0

#Steps to encode

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}


#Steps to decode

<?php 
echo (base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362"))))   #oubWYf2kBq
?>

