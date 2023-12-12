---
category: Leetcode
title: "20. Two Sum"
description: 
author: ["HawkXH"]
tags: ["Stack"]
---

```py
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=  1:
            return False
        stack = []
        dictionary = {"}": "{", "]": "[", ")": "("}
        for item in s:
            if item in ["{", "[", "("]:
                stack.append(item)
            elif item in dictionary:
                if not stack or stack.pop() != dictionary[item]:
                    return False
        return len(stack) == 0
```
