#!/usr/bin/perl

#
# Authentic Theme 18.47 (https://github.com/qooob/authentic-theme)
# Copyright 2015 Alexandr Bezenkov (https://github.com/Real-Gecko/filemin)
# Copyright 2014-2017 Ilia Rostovtsev <programming@rostovtsev.ru>
# Licensed under MIT (https://github.com/qooob/authentic-theme/blob/master/LICENSE)
#

use File::Basename;
use lib ( dirname(__FILE__) . '/../../lib' );

require( dirname(__FILE__) . '/file-manager-lib.pm' );

my %errors;

foreach my $name ( split( /\0/, $in{'name'} ) ) {
    $name = simplify_path($name);
    if ( !&unlink_logged( $cwd . '/' . $name ) ) {
        $errors{ urlize($name) } = "$text{'error_delete'}";
    }
}

redirect( 'list.cgi?path=' . urlize($path) . '&module=' . $in{'module'} . '&error=' . get_errors( \%errors ) );
