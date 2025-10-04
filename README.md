# MIST_Technical_Taskphase
Technical Taskphase during 2nd Year

# 1. Linux Luminarium Questions

## 1) [piping] Split-piping stderr and stdout
The challenge description is as follows:<br>
The challenge here, of course, is that the | operator links the stdout of the left command with the stdin of the right command. Of course, you've used 2>&1 to redirect stderr into stdout and, thus, pipe stderr over, but this then mixes stderr and stdout. How to keep it unmixed?

You will need to combine your knowledge of >(), 2>, and |. How to do it is a task I'll leave to you.<br>

In this challenge, you have:<br>

/challenge/hack: this produces data on stdout and stderr<br>
/challenge/the: you must redirect hack's stderr to this program<br>
/challenge/planet: you must redirect hack's stdout to this program<br>
[Here is the challenge link](https://pwn.college/linux-luminarium/piping/)

### Solving
It took me a decent amount of time to arrive at the answer. I first thought that if i can combine stderr and stdout to stdout, then maybe i can even seperate them into stderr and stdout using process substitution. I was really wrong for thinking that. I ended up using only '>' output redirection and '2>' error redirection to solve the question.
![Image of challenge](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/946feee10efa59bdd8dd553242d1f9ff87234ac1/Stderr%2Cstdin%20and%20stdout.png)

### Flag
> pwn.college{M8x2Bv_KBUffG_zXX9-seTdihUS.dFDNwYDLwcTO3gzW}

## 2) [globbing] Multiple Globs
We put a few happy, but diversely-named files in /challenge/files. Go cd there and run /challenge/run, providing a single argument: a short (3 characters or less) globbed word with two * globs in it that covers every word that contains the letter p. [Here is the challenge Link](https://pwn.college/linux-luminarium/globbing/)

### Solving
This wasn't that hard. I just had to give /challenge/run *p* as they mentioned the glob should be given as an argument. That's it.
![Image of challenge](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/946feee10efa59bdd8dd553242d1f9ff87234ac1/globbing.png)

### Flag
> pwn.college{89Qd5qGNMMSASk3Sm66c7RUH51_.QXycTO2EDLwcTO3gzW}

## 3) [Silly Shenanigans] Snooping on configurations
In this challenge:\
``` 
zardus@dojo:~$ echo "FLAG_GETTER_API_KEY=sk-XXXYYYZZZ" > ~/.bashrc
```
Afterwards, Zardus can easily refer to the API key. In this level, users can use a valid API key to get the flag:\
```
zardus@dojo:~$ flag_getter --key $FLAG_GETTER_API_KEY 
Correct API key! Do you want me to print the key (y/n)? y
pwn.college{HACKED}
zardus@dojo:~$
```
Naturally, Zardus stores his key in .bashrc. Can you steal the key and get the flag?\
[Here is the challenge Link](https://pwn.college/linux-luminarium/shenanigans/)

### Solving
This was simple as well. He had already written it to his .bashrc file. You can read it. So just grep it and then use it as an argument to the flag_getter command. You are asked if you want the flag, obviously you do. Enter y and get the flag.
![Image of challenge](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/946feee10efa59bdd8dd553242d1f9ff87234ac1/snooping%20config.png)

### Flag
> pwn.college{QUQV5YELZlherIXokJz-i9zPAuk.QXyQTM3EDLwcTO3gzW}

# 2. Webex questions

## 1) – HTML- Source code
Don’t search too far.[Here is the challenge Link](https://www.root-me.org/en/Challenges/Web-Server/HTML-Source-code?lang=en)

### Solving
The challenge mentioned to not look far. So i started by inspecting the html code. There i found a comment which mentioned the password. The site mentioned that the password was the flag. So yeah the flag is the password itself. <br><br>
![Image Of Source Code](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/94a438ee34d47bc4c805601ece7f6424ae21846d/Source%20Code.png)

### Flag
> nZ^&@q5&sjJHev0

## 2) – HTTP- IP restriction bypass
Dear colleagues,

We’re now managing connections to the intranet using private IP addresses, so it’s no longer necessary to login with a username / password when you are already connected to the internal company network.

Regards,

The network admin<br>
[Here is the challenge Link](https://www.root-me.org/en/Challenges/Web-Server/HTTP-IP-restriction-bypass)

### Solving 
This required me to know about private networks.<br>
IPv4 Private Address Ranges:<br>
The Internet Assigned Numbers Authority (IANA) has reserved specific ranges of IPv4 addresses for private use. These ranges are as follows:
1. Class A: 10.0.0.0 to 10.255.255.255
2. Class B: 172.16.0.0 to 172.31.255.255
3. Class C: 192.168.0.0 to 192.168.255.255
These addresses can be reused in different private networks around the world without causing conflicts, as they are not routable on the internet.
<br><br>
Given this info, we now know the private addresses range. For an IP - Restriction Bypass, we must add an extra header in the client-request, called : "X-forwarded-for: [The IP Address]". With the above information, we now use any of the 3 and check if it works. We also require Burp Suite here, to intercept the requests, so that we can add the extra header. In my case, i will use 10.0.0.1 as the private network address. <br><br>
![Image of Intercepting Response through Burp Suite Proxy](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/4c16dc89241d789cdfa8a0b4c0de823873a71a7c/IP%20Proxy%20Bypass-1.png)
<br><br>
![Image of adding X-forwarded-for header and receiving its response](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/4c16dc89241d789cdfa8a0b4c0de823873a71a7c/IP%20Proxy%20Bypass-2.png)
<br><br>

### Flag
> Ip_$po0Fing

## 3) – HTTP- Open redirect
Find a way to make a redirection to a domain other than those showed on the web page.<br>
[Here is the challenge Link]([https://www.root-me.org/en/Challenges/Web-Server/HTTP-IP-restriction-bypass](https://www.root-me.org/en/Challenges/Web-Server/HTTP-Open-redirect))<br><br>
[Another link :)](https://www.youtube.com/watch?v=xvFZjo5PgG0)<br><br>

### Solving
A really good explanation of Open Direct, I found on the internet was:<br>
What is an open redirect?<br>
An open redirect vulnerability occurs when an application allows a user to control a redirect or forward to another URL. If the app does not validate untrusted user input, an attacker could supply a URL that redirects an unsuspecting victim from a legitimate domain to an attacker’s phishing site.<br>
The challenge is simple. We have to redirect any of the links to a different website, than the ones mentioned. If you check the headers, it shows that it checks for the hash as well as the domain. You can try only changing the domain and see if the server validates the hash. If it does, you must also change the hash to the domain name you have. Use a hash decoder, to detect the type of hash. In my case, it was an MD5 hash, which allows me to easily encode the hash for my domain and put it in the headers. Send the request and you should be able to see the password in the response. You can intercept the request using Proxy in Burp Suite, then send it to the Repeater. After that,do the required changes, send the request and you will get the response.<br><br>
![Image of Proxy Intercept through Burp Suite](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/4c16dc89241d789cdfa8a0b4c0de823873a71a7c/open%20redirect-1.png)
<br><br>
![Image after receiving the response by addng domain name and fixing the hash](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/4c16dc89241d789cdfa8a0b4c0de823873a71a7c/open%20redirect-2.png)
<br><br>

### Flag
> e6f8a530811d5a479812d7b82fc1a5c5

## 4) – HTTP- User-agent
Admin is really dumb...<br>
[Here is the challenge Link](https://www.root-me.org/en/Challenges/Web-Server/HTTP-User-agent)

### Solving
A user-agent is the software, like a web browser, that a user employs to access the internet and receive content. When you request a webpage, your user-agent sends a "user-agent string" (a message) to the server, identifying the browser type, operating system, and other details. The server uses this information to deliver content formatted specifically for your device and software.<br><br>
You just change User-agent to admin here in the header of it (because he is dumb apparently). After it, just send the request, the response shows the passoword. Pretty straight forward.
![Before Sending the Request](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/94a438ee34d47bc4c805601ece7f6424ae21846d/user%20agent-1.png) <br><br>
![After editing User-Agent and then sending the Request, receiving it's response as well](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/94a438ee34d47bc4c805601ece7f6424ae21846d/user%20agent-2.png)
<br><br>

### Flag
> rr$Li9%L34qd1AAe27

## 5) – HTTP- Directory indexing
CTRL+U...<br>
[Here is the challenge Link](https://www.root-me.org/en/Challenges/Web-Server/HTTP-Directory-indexing)

### Solving
The Source code tells you that there is a page of the website you must visit. There is no route for it on the page, it's just blank. So you must manually edit the link with whatever they have said. Starting /admin being added to the end of the link. Then try pass.html. Well, you see pass.html isn't the page you get your password. But admin has a backup directory. Checking that gives a file which contains the password explicitly.
![Showing source code](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/94a438ee34d47bc4c805601ece7f6424ae21846d/directory%20indexing%20-1.png) <br><br>
![Showing admin page](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/94a438ee34d47bc4c805601ece7f6424ae21846d/directory%20indexing-2.png) <br><br>
![The password file in backup directory](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/94a438ee34d47bc4c805601ece7f6424ae21846d/directory%20indexing-3.png) <br><br>

### Flag
> LINUX

#  3. Cryptography
I had to use tools here. Sometimes even chatgpt (only for the code and frequency analysis,as its a huge file). The last one, i didn't understand much :( , however i have tried it.<br>
# 3.1  3.1 Development
Make a small python script for Hill Cipher, Encryption and Decryption and an option to brute force it with known block size-(2x).

### Python Script And its features:
What it does and its features, along with its limitations: 
1. encrypts and decrypts using a 2×2 Hill cipher key (mod 26)
2. computes matrix inverse mod 26
3. enumerates all invertible 2×2 keys
4. brute-forces keys when you have a known plaintext/ciphertext pair (block size = 2).
5. The script filters input to alphabetic characters only and pads with 'X' to make length divisible by 2.
6. You can adapt the script to preserve non-letter characters or use lowercase mapping as needed.
7. For larger block sizes (3×3 or more) the brute-force space grows as 26^(n^2) and becomes quickly infeasible.
<br>
Using key [[3,3],[2,5]] it encrypted "HELLO" → "HIOZHN" and successfully decrypted back.
<br><br>
Given Below is the python script: <br><br>
```

from math import gcd
from itertools import product

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = 26

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        return None
    return x % m

def matrix_det_2x2(mat):
    return (mat[0]*mat[3] - mat[1]*mat[2]) % M

def matrix_inv_2x2(mat):
    det = matrix_det_2x2(mat)
    inv_det = modinv(det, M)
    if inv_det is None:
        return None
    a, b, c, d = mat
    inv = [( d * inv_det) % M,
           ((-b) * inv_det) % M,
           ((-c) * inv_det) % M,
            ( a * inv_det) % M]
    return inv

def text_to_numbers(text):
    return [ALPHABET.index(ch) for ch in text.upper() if ch.isalpha()]

def numbers_to_text(nums):
    return "".join(ALPHABET[n % M] for n in nums)

def pad_text(text, block_size=2, pad_char='X'):
    filtered = "".join(ch for ch in text.upper() if ch.isalpha())
    if len(filtered) % block_size != 0:
        filtered += pad_char * (block_size - (len(filtered) % block_size))
    return filtered

def encrypt_block(block_nums, key):
    a,b,c,d = key
    x, y = block_nums
    return [(a*x + b*y) % M, (c*x + d*y) % M]

def decrypt_block(block_nums, key_inv):
    return encrypt_block(block_nums, key_inv)

def encrypt(plaintext, key):
    block_size = 2
    pt = pad_text(plaintext, block_size)
    nums = text_to_numbers(pt)
    cipher_nums = []
    for i in range(0, len(nums), block_size):
        block = nums[i:i+block_size]
        cipher_nums.extend(encrypt_block(block, key))
    return numbers_to_text(cipher_nums)

def decrypt(ciphertext, key):
    nums = text_to_numbers(ciphertext)
    inv = matrix_inv_2x2(key)
    if inv is None:
        raise ValueError("Key is not invertible mod 26; can't decrypt.")
    plain_nums = []
    for i in range(0, len(nums), 2):
        block = nums[i:i+2]
        plain_nums.extend(decrypt_block(block, inv))
    return numbers_to_text(plain_nums).rstrip('X')

def all_invertible_2x2_keys():
    for a, b, c, d in product(range(M), repeat=4):
        det = (a*d - b*c) % M
        if gcd(det, M) == 1:
            yield [a,b,c,d]

def brute_force_known_plaintext(ciphertext, known_plaintext):
    ct = pad_text(ciphertext, 2)
    pt = pad_text(known_plaintext, 2)
    if len(ct) != len(pt):
        raise ValueError("Known plaintext and ciphertext lengths must match after filtering/padding.")
    candidates = []
    ct_nums = text_to_numbers(ct)
    pt_nums = text_to_numbers(pt)
    for key in all_invertible_2x2_keys():
        produced = []
        for i in range(0, len(pt_nums), 2):
            produced.extend(encrypt_block(pt_nums[i:i+2], key))
        if produced == ct_nums:
            candidates.append(key)
    return candidates

def key_to_matrix_str(key):
    a,b,c,d = key
    return f"[[{a:2d}, {b:2d}],\n [{c:2d}, {d:2d}]]"

# Simple usage demo if run as a script
if __name__ == "__main__":
    key = [3,3,2,5]  # example key
    plaintext = "HELLO"
    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)
    print("Example key:\n", key_to_matrix_str(key))
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted :", decrypted)

    # Demo brute-force with known plaintext/ciphertext (length 4 example)
    demo_pt = "TEST"
    demo_ct = encrypt(demo_pt, key)
    print("\nBrute-forcing key from known plaintext/ciphertext (demo)...")
    found = brute_force_known_plaintext(demo_ct, demo_pt)
    print(f"Number of candidate keys found: {len(found)}")
    if len(found) <= 20:
        for k in found:
            print(key_to_matrix_str(k))
    else:
        print("Too many results to display; first 20:")
        for k in found[:20]:
            print(key_to_matrix_str(k))

```


# 3.2 Easy Frequency Analysis question where each letter is replaced by an emoji:
cipher: book.txt- can you help my find the name of this book and it’s writer?
[Click here for Link](https://drive.proton.me/urls/7HMYHJQB20#3ssNqYMRXlKp)

### Solving
Frequency analysis is the main method to break simple substitution ciphers (where each symbol → one letter).
The trick:
In English (and most languages), letters don’t appear equally often.
For example:
E is the most common letter (≈13% of text)
then T, A, O, I, N, S, H, R
rare letters: Q, X, Z
So if your ciphertext uses strange symbols (like emojis), the most common symbol is probably E, the second T, and so on.

Basic Methodology:
1. Count character frequencies - Make a histogram of all cipher symbols. Rank them.
2. Guess letter matches - Align cipher frequency order with English frequency order (E,T,A,O,I,N,S,H,R…).
                          → e.g., if 😍 is the most frequent symbol, it probably = E.
3. Look at short words -  1-letter words → “A” or “I”
                          2-letter words → “of”, “to”, “in”, “it”, “is”, etc.
                          3-letter words → “the”, “and”, “for”, “but”
4. Spot repeating patterns - If a word repeats often and fits ??? = “the”, map it.
                             Double symbols → double letters (ll, ss, ee).
5. Use context clues - Capitalized words = proper nouns (names, places).
                       First lines often give the book title or character names.
6. Iterate - Each new mapping reveals more text. The process snowballs until the ciphertext is fully readable.

In Our Case:
1. Look at symbol frequency
I counted how often each emoji appears in the file.
The most common emoji (😍) occurred 141,404 times → that had to be E, the most common letter in English.
The sequence 🤡😢😍 appeared 14,730 times → that looked like “the”, the most common word.
A single emoji (😙) appeared as its own word over 6,000 times → almost certainly “a”.
So right away, the ciphertext was behaving like normal English text.
#### Key emoji → letter mappings used (most important ones):
😍 → e

🤡 → t

😙 → a

🥶 → o

👂 → i

🥴 → n

🥺 → s

😢 → h

🙀 → l

🤐 → y

😵 → p

👧 → u

😡 → m

Align emoji words to plaintext words
For example:
🥺🤡😙🤡😍🙀🤐 → “Stately”
😵🙀👧😡😵 → “plump”
🤪👧😎😂 → “Buck”
😡👧🙀🙀👂🤩😙🥴 → “Mulligan”
🤡😢😍 → “the”
By aligning character-by-character, I built a substitution table (emoji → letters).

By Applying to next 300 characters,we get:
stately, plump buck mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed...
That’s the exact opening of *Ulysses*.

Therefore the author and book is: *Ulysses by James Joyce*.

### Flag(Answer)
> Ulysses by James Joyce

# 3.3 Spiral cipher
cipher:taskphaWL_PL4sOingpYefdngaP{_diddL40ap}y5rn_s1m37

### Solving
Used the spiral cipher decode tool from dcode. [Click for the tool](https://www.dcode.fr/spiral-cipher) <br>
One thing that is clearly evident, is that the flag is in form of taskphase{...}. So i was sure it should be somewhat in that form. Used the spiral cipher decode tool from dcode that brute forced it in different types of spiral ciphers.  Got the 2nd option that best matches what I was looking for. I think the type of spiral cipher here is: Inward from top-left, clockwise , because thats what it showed for the second option. So yeah that's the flag :) . 
![Image of spiral cipher decode tool with 2nd ](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/38f9808d22d4ae9b0a42e95b0b8c9f539a812959/spiral%20cipher.png)

### Flag
> taskphase{4r73m1s_n0_fOWL_PL4YPL5y}paddingpadding

# 3.4 Averages 3 letters to make cipher
cipher: GGGIIIFFFIIIGGGDDDGGGAAABBB
Didn't understand this question (my skill issue). I did try something through Chatgpt. <br>

### Solving
Collapse every triple:
GGG III FFF III GGG DDD GGG AAA BBB → GIFIGDGAB.<br>
Pattern of collapsed letters = A B C B A D A E F → positions 1,5,7 are same; 2 and 4 are same. That strongly suggests a phrase where word1 and the first letter of word3 repeat at those positions.<br>
From pattern-matching with common 3-letter words, the first three letters consistently map to ONE (i.e. G→O, I→N, F→E). That anchor is very strong.<br>
Of the plausible 3-word combinations that fit the pattern and are grammatical/readable, “ONE NOW OUT” is the clearest English phrase (“one now out” — e.g. “one [player/thing] is now out”), so I pick it as the answer.<br><br>

### Flag
> ONENOWOUT
