---
category: Leetcode
title: "1. Two Sum"
description: 
author: ["HawkXH"]
tags: ["Simple"]
---

```py
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Create a dictionary to store num:index mapping

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index

        return []  # Return an empty list if no two numbers add up to the target
```
