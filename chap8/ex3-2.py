s1 = 'this is a test';
s2 = 'this is another test';

out = list(set(s1) & set(s2));
out.remove(' ');

print("common chars are:", end=' ');
print(*out, sep=', ');
