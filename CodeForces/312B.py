# https://codeforces.com/problemset/problem/312/B?fbclid=IwY2xjawOs7KJleHRuA2FlbQIxMABicmlkETA5NFFiZ3c1eFNrYUdFNDBxc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHsEewBbRAX6thPrvuaQRijOX0O_VBNwZleQ12nywUeJb6OD5PkXNH6YLqBHL_aem_zd_UJbbdoJDkSoPfoFCqlg



A, B, C, D = map(int, input().split())


SmallChange = A / B
BigChange = C / D

#formel fundet: https://math.stackexchange.com/questions/3396500/two-players-shooting-a-target-alternately

ChangeSmallWins = SmallChange / (SmallChange + BigChange - SmallChange*BigChange)

print( ChangeSmallWins )
