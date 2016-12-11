def read_input(filename):
    """Read in a text file and onvert to list separated by new lines."""
    with open(filename, "r") as f:
        text = f.read().splitlines()
    return text


def find_pieces(ip):
    """Split ip string into string and a list of substrings that were within brackets."""
    import re

    in_brackets = r"\[(\w+)\]"
    m = set(re.findall(in_brackets, ip))
    ip = set(re.split(in_brackets, ip)) - m

    return m, ip


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
        m, ip = find_pieces(ip)
        if not sum(check_mirror(s) for s in m):
            if sum(check_mirror(i) for i in ip):
                count += 1
    return count


def get_abas(ips):
    abas = []

    for ip in ips:
        for i, char in enumerate(ip):
            if(
                i > 0 and
                i + 2 < len(ip) and
                char == ip[i + 2] and
                char != ip[i + 1]
            ):
                abas.append(ip[i:i + 3])
    return abas


def get_babs_from_abas(abas):
    babs = []
    for aba in abas:
        babs.append(aba[1] + aba[0] + aba[1])
    return babs


def check_babs(ms, babs):
    for m in ms:
        for bab in babs:
            print(bab, m)
            if bab in m:
                print("is substring")
                return True
    return False


def count_ssl_supporting_ips(ips):
    count = 0
    for ip in ips:
        m, ip = find_pieces(ip)
        babs = get_babs_from_abas(get_abas(ip))
        if check_babs(m, babs):
            count += 1
    return count


if __name__ == "__main__":
    filename = "input/day-7-input.txt"
    ips = read_input(filename)
    print(count_tls_supporting_ips(ips))
    print(count_ssl_supporting_ips(ips))
