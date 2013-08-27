use strict;
use warnings;

my $x = $ARGV[0];
my $y = $ARGV[1];

my $offset = 0;
my $last_offset;
my $count = 0;

sub getYtype {
	my $y = shift;
	my $char_list;
	for (my $i = 0; $i < length $y; $i++) {
		my $char = substr $y, $i, 1;
		$char_list->{$char} = 1;

		if (keys %$char_list > 2){
			return keys %$char_list;
		}
	}
	return keys %$char_list;
}

sub find_min {
	my $offset = shift;
	my $first = shift;
	my $last = shift;

	my $left = 0;
	my $right = 0;
	while ((substr $x, ($offset - $left), 1) eq $first){		
		$left++;
	}

	while ((substr $x, ($offset + $right + (length $y) - 1), 1) eq $last){
		$right++;
	}

	return [($left >= $right) ? $right : $left, ($left >= $right)];
}

my $type = getYtype($y);
print "type: $type\n";

while (1) {
	print "index: " . (index $x, $y, $offset) . "\n";
	if ((index $x, $y, $offset) < 0){
		last;
	}else{
		$offset = index $x, $y, $offset;

		if ($type > 2){
			$count++;
			print "count++\n";
			if (defined $last_offset and $offset - $last_offset < length $y and $offset != 0){
				$count--;
				$last_offset = $offset;
				$offset += (length $y) - 1;
				print "conut--\n";
			}else{
				$last_offset = $offset;
			}
		$offset++;
		}else{
			my ($min, $direction) = @{find_min($offset, (substr $y, 0, 1), (substr $y, -1, 1))};
			print "sub_min: $min\n";
			print "direction: $direction\n";
			$count += $min;
			if ($direction) {
				$offset += $min;
			}else{
				$offset++;
			}
		}

		print "offset: $offset\n";
	}
}

print "min: $count\n";

