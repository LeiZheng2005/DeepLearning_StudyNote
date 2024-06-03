# 00.SSL_Paper

准备从这里的Readme寻找一些合适的论文学习，写一些学习笔记。https://github.com/HiLab-git/SSL4MIS

由于都是半监督医学图像分割论文，故标题中的Semi-supervised Medical Image Segmentation省略不写。

>  刚刚在csdn看到Hinton的采访文章(中文):https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/139105929?spm=1000.2115.3001.5926 

>  youtube原视频:https://www.youtube.com/watch?v=n4IQOBka8bc

> 今晚抽时间好好看一下学习一下，文章大致看了，到时候也写一篇笔记。

~~leizheng你居然没有记笔记这个，这啥时候写的现在都24.06.03了我看你也没写笔记~~

# 01.Class imbalance

知乎上的中文博客：类不平衡问题Class imbalance https://zhuanlan.zhihu.com/p/94599093

想做这一个方向的工作，能看懂的话今晚找师兄讨论可行性。

~~不可行，不可行，换一个方向,2024.06.03~~

另一个博客：

[干货总结] 常见的类别不平衡问题解决方法https://zhuanlan.zhihu.com/p/556158050

csdn上的：样本不均衡及其解决办法 https://blog.csdn.net/qq_40006058/article/details/121070512

知乎上的： 采用半监督进行医学图像分割，为什么效果没有很大提升？ https://www.zhihu.com/question/537654720/answer/3084586769

# 02.Debiased Self-Training

> 这一篇是DHC for Class-imbalanced的基础，讲的是消除偏差自训练
>
> Debiased Self-Training for Semi-Supervised Learning

> github:
>
> https://github.com/thuml/Debiased-Self-Training
>
> paper: NIPS
>
> https://openreview.net/pdf?id=NI7moUOKtc
>
> zhihu:
>
> https://zhuanlan.zhihu.com/p/602133116

主要讲的是**半监督模型中会出现好的越好，坏的越坏的情况**。原因在于**训练的伪标签的正确与否，导致模型的优化方向趋于不同**。解决方法就是**通过一个代理分类器判断伪标签的利用，主要是使用有标签的生成的高质量的伪标签**，为防止过拟合于少量样本，使用伪标签训练，具体看知乎原作者的博客文章，链接在上面。

~~wok，清华大学！这好像是A类会议吧，呜呜呜，发SCI无望了，知道发顶会有多难了吧。这篇文章的具体实现我还不会，先不看代码实现吧，现在看效率太低了，先看文章，看思路，代码链接放在这里就欧克。~~

# 03.Addressing class imbalance

>Addressing Class Imbalance in Semi-supervised Image Segmentation: A Study on Cardiac MRI
>
>github:
>
>
>
>paper:
>
>https://arxiv.org/pdf/2209.00123
>
>> zhihu:
>>
>> 简要介绍：https://zhuanlan.zhihu.com/p/561294076?utm_id=0
>>
>> ​        由于数据不平衡和有限，半监督的医学图像分割方法通常无法为某些特定的尾部类别产生卓越的性能。对这些特定课程的培训不足可能会引入更多的噪音，从而影响整体学习。为了减轻这一缺点并确定表现不佳的课程，我们建议保持一个信心阵列，以记录培训期间的班级表现。提出了这些置信分数的模糊融合，以适应每个样本中的个人置信度指标，而不是传统的合奏方法，其中为所有测试案例分配了一组预定义的固定权重。此外，我们引入了一种强大的班级抽样方法和动态稳定，以获得更好的训练策略。我们提出的方法考虑了所有表现不佳的班级，并具有动态权重，并试图在训练过程中消除大多数噪音。通过对两个心脏MRI数据集进行评估，ACDC和MMWHS，我们提出的方法显示出有效性和概括性，并且优于文献中发现的几种最先进的方法。

关于类别不均衡和mean-Teacher的关系有点想法了：学生要进行高考，为了帮助学生取得好成绩，老师会整理这个科目的大纲和重点，书本上每一个章节的重难点都不一样。在准备高考的这三年里，老师会给学生做随堂测试，章节测试，期中测试，期末测试还有数不完的模拟测试。学生会在老师讲解之后学习巩固没有学会的知识点。假设总共考6本书的内容，共计60章节，老师认为有些章节是重点，模拟测试经常出这个题目，于是类不均衡了。而这个不均衡的比例如果和高考是一致的，那成绩必然很好，但如果不均衡的比例和高考不一致，那么成绩就会非常低。这就是正样本越好，负样本越差。

简单的说一个二分类吧，假设高考题目只有两种体型，一个是A，一个是B。往年的比例大概是90%的题目是A题型，10%的题型是B。那么对于老师来说我给学生也是这么教，90%学A题型，10%学B，那么有些人就会想，那我只要90分不就行了，我一直学A，你给我教B，我也学A，我先把A学清楚，少花时间在B身上，对于优化器来说这个学生确实在往好的方面发展，A的比重大，成绩高。但是如果今年高考是10%是A，90%是B的话，那学生的成绩不就是很低吗。我觉得大概就是这个意思，在分割中对应像素的大小，黑色的多，效果好，分数高，那我都判定是黑色不就好了，哪怕错了我再改成白色不就行了。



# 04.A systematic study of the class imbalance problem in CNN

>paper:
>
>https://arxiv.org/pdf/1710.05381
>
>csdn:
>
>中文博客：https://blog.csdn.net/qq_37151108/article/details/105344107?ops_request_misc=&request_id=&biz_id=102&utm_term=Addressing%20class%20imbalance%20in%20&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-105344107.142

# 05.DHC for Class-imbalanced

> github:
>
> https://github.com/xmed-lab/DHC
>
> paper: MICCAI2023
>
> https://arxiv.org/pdf/2307.11960
>
> csdn：
>
> - 一篇简短的参考文章:https://blog.csdn.net/qq_45745941/article/details/138604262?ops_request_misc=&request_id=&biz_id=102&utm_term=DHC:%20Dual-debiased%20Heterogeneo&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-138604262.142
>
> - arxiv合集文章速递介绍:https://blog.csdn.net/wzk4869/article/details/131919388?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171636364616800213070587%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171636364616800213070587&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-131919388-null-null.142
>
> zhihu：
>
> 类不平衡问题：https://zhuanlan.zhihu.com/p/94599093

