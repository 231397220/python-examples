# 为以下 sql 语句标注执行顺序：

```sql
SELECT DISTINCT player_id, player_name, count(*) as num   # 5
FROM player JOIN team ON player.team_id = team.team_id    # 1
WHERE height > 1.80                                       # 2
GROUP BY player.team_id                                   # 3
HAVING num > 2                                            # 4
ORDER BY num DESC                                         # 6
LIMIT 2                                                   # 7
```

-- Step1：FROM JOIN ON：player + team通过筛选生成新的虚拟表；
-- Step2：WHERE ： 进一步筛选形成虚拟表；
-- Step3：GROUP BY 执行分组操作
-- Step4：HAVING 进行筛选，生成虚拟表
-- Step5：SELECT 从上一个虚拟表中进行不重复字段查询
-- Step6：ORDER 对查询结果进行降序排序
-- Step7：LIMIT 取2条查询结果