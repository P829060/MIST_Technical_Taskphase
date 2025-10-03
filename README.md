<img width="1918" height="967" alt="image" src="https://github.com/user-attachments/assets/50ed077d-d8f8-4934-afd8-5a410f079569" /># MIST_Technical_Taskphase
Technical Taskphase during 2nd Year

# 1. Linux Luminarium Questions

## 1) [piping] Split-piping stderr and stdout
The challenge description is as follows:\ 
The challenge here, of course, is that the | operator links the stdout of the left command with the stdin of the right command. Of course, you've used 2>&1 to redirect stderr into stdout and, thus, pipe stderr over, but this then mixes stderr and stdout. How to keep it unmixed?

You will need to combine your knowledge of >(), 2>, and |. How to do it is a task I'll leave to you.\

In this challenge, you have:\

/challenge/hack: this produces data on stdout and stderr\
/challenge/the: you must redirect hack's stderr to this program\
/challenge/planet: you must redirect hack's stdout to this program\
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
Don’t search too far

### Solving
The challenge mentioned to not look far. So i started by inspecting the html code. There i found a comment which mentioned the password. The site mentioned that the password was the flag. So yeah the flag is the password itself

### Flag
> nZ^&@q5&sjJHev0

## 2) – HTTP- IP restriction bypass
Dear colleagues,

We’re now managing connections to the intranet using private IP addresses, so it’s no longer necessary to login with a username / password when you are already connected to the internal company network.

Regards,

The network admin

### Solving 
This required me to know about private networks.
IPv4 Private Address Ranges:
The Internet Assigned Numbers Authority (IANA) has reserved specific ranges of IPv4 addresses for private use. These ranges are as follows:
Class A: 10.0.0.0 to 10.255.255.255
Class B: 172.16.0.0 to 172.31.255.255
Class C: 192.168.0.0 to 192.168.255.255
These addresses can be reused in different private networks around the world without causing conflicts, as they are not routable on the internet.

Given this info, we now know the private addresses range. For an IP - Restriction Bypass, we must add an extra header in the client-request, called : "X-forwarded-for: [The IP Address]". With the above information, we now use any of the 3 and check if it works. We also require Burp Suite here, to intercept the requests, so that we can add the extra header. In my case, i will use 10.0.0.1 as the private network address.

### Flag
> Ip_$po0Fing

## 3) – HTTP- Open redirect


### Flag
> e6f8a530811d5a479812d7b82fc1a5c5

## 4) – HTTP- User-agent

### Flag
> rr$Li9%L34qd1AAe27

## 5) – HTTP- Directory indexing

### Flag
> LINUX

#  3. Cryptography
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

### Flag
> taskphase{4r73m1s_n0_fOWL_PL4YPL5y}paddingpadding

# 3.4 Averages 3 letters to make cipher
cipher: GGGIIIFFFIIIGGGDDDGGGAAABBB

### Solving

### Flag
> 
