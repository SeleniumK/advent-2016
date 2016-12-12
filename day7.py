def read_input(filename):
    """Read in a text file and onvert to list separated by new lines."""
    with open(filename, "r") as f:
        text = f.read().splitlines()
    return text


def find_pieces(ip):
    """Split ip string into string and a list of substrings that were within brackets."""
    import re

    in_brackets = r"\[(\w+)\]"
    hypernet = set(re.findall(in_brackets, ip))
    ip = set(re.split(in_brackets, ip)) - hypernet

    return hypernet, ip


def check_mirror(string):
    """Check given string for a 4 character mirror pattern.

    EX. xyyx returns true.
        baaq returns false.
    Does not support duplicate values:
        aaaa returns false.
    """
    for i, char in enumerate(string):
        if (
            i + 2 < len(string) and
            i > 0 and
            char == string[i + 1] and
            string[i - 1] == string[i + 2] and
            char != string[i - 1]
        ):
            return True
    return False


def count_tls_supporting_ips(ips):
    """Given a list, return a count where m has no mirroring and the ip string does."""
    count = 0
    for ip in ips:
        hypernet, ip = find_pieces(ip)
        if not sum(check_mirror(s) for s in hypernet):
            if sum(check_mirror(i) for i in ip):
                count += 1
    return count

    # return sum(
    #     (not sum(check_mirror(s) for s in hypernet)) and
    #     (sum(check_mirror(i) for i in ip))
    #     for ip in ips for hypernet, ip in find_pieces(ip)
    # )


def get_abas(ips):
    def cond(i, char, ip):
        return (
            i > 0 and
            i + 2 < len(ip) and
            char == ip[i + 2] and
            char != ip[i + 1]
        )
    return [ip[i:i + 3] for ip in ips for i, char in enumerate(ip) if cond(i, char, ip)]


def get_babs_from_abas(abas):
    return [aba[1::] + aba[1] for aba in abas]


def check_babs(hypernet, babs):
    return any(bab in h for bab in babs for h in hypernet)


def count_ssl_supporting_ips(ips):
    count = 0
    for ip in ips:
        h, i = find_pieces(ip)
        count += check_babs(h, get_babs_from_abas(get_abas(i)))
    return count

    # return sum(
    #     check_babs(h, get_babs_from_abas(get_abas(i))) for ip in ips for h, i in find_pieces(ip)
    # )


if __name__ == "__main__":
    filename = "input/day-7-input.txt"
    ips = read_input(filename)
    print(count_tls_supporting_ips(ips))
    print(count_ssl_supporting_ips(ips))
