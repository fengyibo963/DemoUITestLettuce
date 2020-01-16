# language: zh-CN

特性: UI自动化测试模版

  场景: 亚马逊商城搜索商品,并检验深圳南山区有货
    Given 我打开谷歌浏览器
    And 我访问亚马逊首页
    When 我在"首页_搜索输入框"中输入"牙刷"
    And 我点击"首页_搜索按钮"
    And 我点击一下文本"儿童牙刷 1岁半-5岁用 面包超人 黄色 8本"，如果文本不存在，我将点击"商品列表页面_下一页按钮"后再次尝试点击，最多10次
    And 我切换到浏览器第2个页签
    And 我点击"商品详情页面_配送区域选择框"
    And 我点击"商品详情页面_配送区域(省份)选择框"
    And 我点击文本"广东"
    And 我点击"商品详情页面_配送区域(城市)选择框"
    And 我点击文本"深圳市"
    And 我点击"商品详情页面_配送区域(区/县)选择框"
    And 我点击文本"南山区"
    Then 我获取"商品详情页面_现货情况"文本内容
    And 我比较文本与"现在有货"是否相等
    And 我关闭浏览器或设备
