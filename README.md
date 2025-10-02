# MIST_Technical_Taskphase
Technical Taskphase during 2nd Year

## Linux Luminarium Questions
### [piping] Split-piping stderr and stdout
The challenge description is as follows:\ 
The challenge here, of course, is that the | operator links the stdout of the left command with the stdin of the right command. Of course, you've used 2>&1 to redirect stderr into stdout and, thus, pipe stderr over, but this then mixes stderr and stdout. How to keep it unmixed?

You will need to combine your knowledge of >(), 2>, and |. How to do it is a task I'll leave to you.\

In this challenge, you have:\

/challenge/hack: this produces data on stdout and stderr\
/challenge/the: you must redirect hack's stderr to this program\
/challenge/planet: you must redirect hack's stdout to this program\
[Here is the challenge link](https://pwn.college/linux-luminarium/piping/)

#### Solving
It took me a decent amount of time to arrive at the answer. I first thought that if i can combine stderr and stdout to stdout, then maybe i can even seperate them into stderr and stdout using process substitution. I was really wrong for thinking that. I ended up using only '>' output redirection and '2>' error redirection to solve the question.
![Image of challenge](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/946feee10efa59bdd8dd553242d1f9ff87234ac1/Stderr%2Cstdin%20and%20stdout.png)

#### Flag
> pwn.college{M8x2Bv_KBUffG_zXX9-seTdihUS.dFDNwYDLwcTO3gzW}

### [globbing] Multiple Globs
We put a few happy, but diversely-named files in /challenge/files. Go cd there and run /challenge/run, providing a single argument: a short (3 characters or less) globbed word with two * globs in it that covers every word that contains the letter p. [Here is the challenge Link](https://pwn.college/linux-luminarium/globbing/)

#### Solving
This wasn't that hard. I just had to give /challenge/run *p* as they mentioned the glob should be given as an argument. That's it.
![Image of challenge](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/946feee10efa59bdd8dd553242d1f9ff87234ac1/globbing.png)

#### Flag
> pwn.college{89Qd5qGNMMSASk3Sm66c7RUH51_.QXycTO2EDLwcTO3gzW}

### [Silly Shenanigans] Snooping on configurations
In this challenge:\
''' zardus@dojo:~$ echo "FLAG_GETTER_API_KEY=sk-XXXYYYZZZ" > ~/.bashrc '''
Afterwards, Zardus can easily refer to the API key. In this level, users can use a valid API key to get the flag:\
''' zardus@dojo:~$ flag_getter --key $FLAG_GETTER_API_KEY 
Correct API key! Do you want me to print the key (y/n)? y
pwn.college{HACKED}
zardus@dojo:~$ '''
Naturally, Zardus stores his key in .bashrc. Can you steal the key and get the flag?\
[[Here is the challenge Link](https://pwn.college/linux-luminarium/shenanigans/)

#### Solving
This was simple as well. He had already written it to his .bashrc file. You can read it. So just grep it and then use it as an argument to the flag_getter command. You are asked if you want the flag, obviously you do. Enter y and get the flag.
![Image of challenge](https://github.com/P829060/LinuxLuminariumAndBanditImages/blob/946feee10efa59bdd8dd553242d1f9ff87234ac1/snooping%20config.png)

#### Flag
> pwn.college{QUQV5YELZlherIXokJz-i9zPAuk.QXyQTM3EDLwcTO3gzW}
