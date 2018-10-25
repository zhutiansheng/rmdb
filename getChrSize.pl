#!/usr/bin/perl
open myfile,"all.con" or die "Can not open file";
my $chr_length=0;
my $chr;
my $begin=1;
while(my $line=<myfile>){
	if($begin){$begin=0;if($line=~/>(.*)/){$chr=$1;};next;}
	if($line=~/>(.*)/){
	print $chr;
	print "\t";
	print ($chr_length);
	print "\n";
	$chr=$1;
	$chr_length=0;
	}
	else {
	$line=~s/\r\n//g;
	$chr_length+=length($line);
	}
}
close(myfile);
print "$chr\t$chr_length\n";
