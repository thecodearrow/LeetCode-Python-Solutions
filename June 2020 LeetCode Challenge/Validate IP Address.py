"""
#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3362/

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.


"""
class Solution:
    def isValidIP4(self,IP):
        if("." not in IP):
            return False
        split_IP=IP.split(".")
        if(len(split_IP)!=4):
            #check for 4 groups
            return False
        valid_chars=set()
        for i in range(10):
            valid_chars.add(str(i))
        for ip in split_IP:
            if(len(ip)==0):
                return False
            if(ip[0]=='0' and len(ip)!=1):
                #check for leading zeros!
                return False
            for c in ip:
                if(c not in valid_chars):
                    return False
            int_ip=int(ip)
            if(not(int_ip>=0 and int_ip<=255)):
                #check range!
                return False
            
        
        return True
            
        
    def isValidIP6(self,IP):
        if(":" not in IP):
            return False
        valid_chars=set(['a','b','c','d','e','f','A','B','C','D','E','F'])
        for i in range(10):
            valid_chars.add(str(i))
        split_IP=IP.split(":")
        if(len(split_IP)!=8):
            #check for 8 groups!
            return False
        for ip in split_IP:
            if(len(ip)>4 or len(ip)==0):
                #extra padding or empty
                return False
            
            for c in ip:
                if(c not in valid_chars):
                    return False
        
        return True
            
        
    def validIPAddress(self, IP: str) -> str:
        if(self.isValidIP4(IP)):
            return "IPv4"
        if(self.isValidIP6(IP)):
            return "IPv6"
        return "Neither"