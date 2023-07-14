<?php
    phpinfo();

    // 
?>
Installation
Install the extension: Press F1, type ext install php-debug.

This extension is a debug adapter between VS Code and Xdebug by Derick Rethans. Xdebug is a PHP extension (a .so file on Linux and a .dll on Windows) that needs to be installed on your server.

Install Xdebug I highly recommend you make a simple test.php file, put a phpinfo(); statement in there, then copy the output and paste it into the Xdebug installation wizard. It will analyze it and give you tailored installation instructions for your environment. In short:

On Windows: Download the appropriate precompiled DLL for your PHP version, architecture (64/32 Bit), thread safety (TS/NTS) and Visual Studio compiler version and place it in your PHP extension folder.
On Linux: Either download the source code as a tarball or clone it with git, then compile it. Or see if your distribution already offers prebuilt packages.
Configure PHP to use Xdebug by adding zend_extension=path/to/xdebug to your php.ini. The path of your php.ini is shown in your phpinfo() output under "Loaded Configuration File".

Enable remote debugging in your php.ini:

For Xdebug v3.x.x:

xdebug.mode = debug
xdebug.start_with_request = yes

For Xdebug v2.x.x:

xdebug.remote_enable = 1
xdebug.remote_autostart = 1
xdebug.remote_port = 9000

There are other ways to tell Xdebug to connect to a remote debugger, like cookies, query parameters or browser extensions. I recommend remote_autostart (Xdebug v2)/start_with_request (Xdebug v3) because it "just works". There are also a variety of other options, like the port, please see the Xdebug documentation on remote debugging for more information. Please note that the default Xdebug port changed between Xdebug v2 to v3 from 9000 to 9003.

If you are doing web development, don't forget to restart your webserver to reload the settings.

Verify your installation by checking your phpinfo() output for an Xdebug section.