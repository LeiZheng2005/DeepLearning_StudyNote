# SSL_MIS_Note

### 01.DHC: Dual-debiased Heterogeneous Co-training Framework for Class-imbalanced Semi-supervised Medical Image Segmentation

这一篇讲的是类不均衡，用双除偏异构协同训练框架。

类不均衡的出现是不同类别的训练样例数目差别很大，造成的模型训练的偏差，具体可见这个路径的md文件(DeepLearning_StudyNote/Semi_Supervised_Learning_Medical_Image_Segmentation/Note/Class_Imbalance/Class_Imbalance_Note.md)

解决的办法有欠采样，过采样，调整权重等等。

### 02.Consistency-guided Meta-Learning for Bootstrapping Semi-Supervised Medical Image Segmentation

[csdn博客链接](https://blog.csdn.net/qq_45745941/article/details/131910007?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171643340916800225564282%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171643340916800225564282&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-131910007-null-null.142)这一篇相当于是改进meanTeacher使用了逐像素权重映射系统，动态为初始化的标签和模型预测分配权重，利用元过程确定，基于精准注释的图像让伪标签增强PLE，在干净的数据集上自我引导。

### 03.Uncertainty-guided dual-views for semi-supervised volumetric medical image segmentation

[csdn博客链接](https://blog.csdn.net/Rad1ant_up/article/details/135177477?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171643448416800211572132%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171643448416800211572132&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-135177477-null-null.142)这篇讲的是多视角不确定性引导在半监督体积医学图像分割上的应用。在医学图像中运用多视角有两方面的挑战，1是保证同一个数据在不同视图中存在差异，2是需要通过估计伪标签来消除不确定性样本的影响。本文的解决方法是基于对抗学习的双视角协同框架对每一个视图的高置信预测中学习到有用的知识，确保两个视图都可以有靠谱的预测，两个网络取长补短。

### 04.Correlation-Aware Mutual Learning for Semi-supervised Medical Image Segmentation

论文地址：https://arxiv.org/abs/2307.06312

[csdn简要介绍](https://blog.csdn.net/wzk4869/article/details/131711976?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171643509116800185835579%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171643509116800185835579&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-131711976-null-null.142)一个新的相关感知相互学习框架，利用标记数据指导未标记数据提取信。基于相互学习的策略：两个模块，一个是交叉样本相互注意模块CMA，一个是全相关性一致模块OCC。CMA模块在一组样本之间建立密集的交叉样本相关性，使得标签先验知识能够转移到未标记的数据。OCC模块构造未标记数据集和标记数据集之间的全相关性，并通过约束每个子模型的全相关矩阵一致来正则化对偶模型。 

### 05.Ambiguity-selective consistency regularization for mean-teacher semi-supervised medical image segmentation

歧义选择性一致性正则化 均值教师半监督医学图像分割 这一篇好像之前看过，先放这里，图片也找不到，引用次数25。先放着，等会补上。

~~不是你咋都没看，虽然现在看来确实不需要看了，好吧2024.06.03~~

### 06.C3PS: Context-aware Conditional Cross Pseudo Supervision for Semi-supervised Medical Image Segmentation

C3PS：半监督医学图像分割的上下文感知条件交叉伪监督
题目有些看不懂，先补充一下相关知识

#### Context-aware / Sequencial / Session-based 的区别

[知乎链接](https://zhuanlan.zhihu.com/p/124324598)

### 07.Cross-supervised Dual Classifiers for Semi-supervised Medical Image Segmentation

用于半监督医学图像分割的交叉监督双分类器

### 08.Self-aware and Cross-sample Prototypical Learning for Semi-supervised Medical Image Segmentation

半监督医学图像分割的自我意识和跨样本原型学习

第7篇和第8篇的作者是同一团队，两篇文章代码均未开源，有可能是没有找到。

[微信公众号链接](https://mp.weixin.qq.com/s?__biz=MzU1MzY0MDI2NA==&mid=2247501087&idx=1&sn=b150f0a41406facc49cd74832e45f64a&chksm=fbed4d38cc9ac42e478d09b596da04a55d625460d5b93a2adcf54f12ef95ecf828cdeb10fb5e&scene=178&cur_album_id=2870189585774116867#rd)以及[csdn博客链接](https://blog.csdn.net/m0_61899108/article/details/131160097?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171644031116800178557076%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171644031116800178557076&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-131160097-null-null.142)代码未开源。本文提出了一种自**感知和跨样本原型学习方法**（SCP-Net）

### 09.Orthogonal Annotation Benefits Barely-supervised Medical Image Segmentation

正交注释有利于无监督的医学图像分割 cvpr2023

[csdn正交注释有利于无监督的医学图像分割](https://blog.csdn.net/qq_45745941/article/details/131241057?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171644084716800225536086%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171644084716800225536086&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-131241057-null-null.142^v100^pc_search_result_base2&utm_term=Orthogonal%20Annotation%20Benefits%20Barely-supervised%20Medical%20Image%20Segmentation&spm=1018.2226.3001.4187) [csdn博客](https://blog.csdn.net/weixin_53841792/article/details/132004310?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171644084716800225536086%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171644084716800225536086&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-132004310-null-null.142) [zhihu论文原作者博客](https://zhuanlan.zhihu.com/p/623844173)

[文章地址](https://arxiv.org/pdf/2303.13090) [代码地址](https://github.com/HengCai-NJU/DeSCO)

利用正交标注从多视角进行图像分割，并采用了配准产生密集伪标签，再进行标签融合，通过不同的权重动态更新，从密集到悉数的协同训练。

### 10.Pseudo-Label Guided Contrastive Learning for Semi-Supervised Medical Image Segmentation

用于半监督医学图像分割的伪标签引导对比学习

[csdn博客地址](https://blog.csdn.net/qq_43656233/article/details/132533386?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171644194716800180637531%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171644194716800180637531&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-132533386-null-null.142) [csdn另一篇](https://blog.csdn.net/qq_42854305/article/details/131735186?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171644194716800180637531%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171644194716800180637531&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-131735186-null-null.142)  ~~这篇论文 对比学习还是挺难的呜呜呜～先写到这里，睡会午觉～~~