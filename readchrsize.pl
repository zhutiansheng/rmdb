use Bio::DB::Fasta;
#��һ�оͲ��ý����˰ɣ�����Bio::DB::Fastaģ��

  # create database from directory of fasta files
  my $db      = Bio::DB::Fasta->new('all.con');
my $obj     = $db->get_Seq_by_id('CHROMOSOME_I');
my $length  = $obj->length;
print $length;

