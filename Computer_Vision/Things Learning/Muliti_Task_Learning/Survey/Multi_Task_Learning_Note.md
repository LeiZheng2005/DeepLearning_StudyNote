# Multi_Task_Learning_Note

多任务学习通过划分小认为共享参数权重，更快地训练模型。广义地说含有多个loss函数就可以叫做是多任务学习。

从课程学习相结合来说的话，有先验知识，然后给样本划分难度进行识别，也就是说可以结合相关领域的。

> 以下来自参考文章：多任务学习（Multi-Task Learning, MTL）
>
> 目标：通过权衡主任务与辅助的相关任务中的训练信息来提升模型的泛化性与表现。从机器学习的视角来看，**MTL可以看作一种inductive transfer**（[先验知识](https://so.csdn.net/so/search?q=先验知识&spm=1001.2101.3001.7020)），**通过提供inductive bias**（某种对模型的先验假设）**来提升模型效果**。比如，**使用L1正则，我们对模型的假设模型偏向于sparse solution**（参数要少）。**在MTL中，这种先验是通过auxiliary task来提供**，更灵活，告诉模型偏向一些其他任务，最终导致模型会泛化得更好。

> 多任务学习（Multi-Task Learning, MTL）
>
> https://blog.csdn.net/laolu1573/article/details/78205180/?ops_request_misc=&request_id=&biz_id=102&utm_term=%E5%A4%9A%E4%BB%BB%E5%8A%A1%E8%AF%BE%E7%A8%8B%E5%AD%A6%E4%B9%A0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-6-78205180.142
>
> Multi-task Learning(Review)多任务学习概述
>
> https://zhuanlan.zhihu.com/p/59413549
>
> **An Overview of Multi-Task Learning in Deep Neural Networks**
>
> https://arxiv.org/abs/1706.0509