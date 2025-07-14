---  
glightbox: false  # 禁用当前页面的灯箱效果  
---  

<style>
/* 定义自适应网格布局 */
.product-list {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 15px;
  margin: 1rem 0;
}

/* 响应式布局 - 平板设备 (小于1024px) */
@media (max-width: 1024px) {
  .product-list {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

/* 响应式布局 - 手机设备 (小于768px) */
@media (max-width: 768px) {
  .product-list {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
  }
}

/* 响应式布局 - 小型手机设备 (小于480px) */
@media (max-width: 480px) {
  .product-list {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
}

.product-list a {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: inherit;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  padding: 12px;
  transition: all 0.3s ease;
  height: 100%;
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.product-list a:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  border-color: rgba(0, 0, 0, 0.2);
}

.product-list img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
  margin-bottom: 15px;
  object-fit: contain;
}

/* 响应式图片尺寸调整 */
@media (max-width: 768px) {
  .product-list img {
    max-height: 150px;
  }
}

@media (max-width: 480px) {
  .product-list img {
    max-height: 180px;
  }
}

.product-list h2 {
  color: #0066cc;
  font-size: 18px;
  font-weight: bold;
  text-align: center;
  margin: 0;
  padding: 0;
}

.product-list .model-alias {
  color: #666;
  font-size: 16px;
  text-align: center;
  margin-top: 5px;
}
</style>


# User Guide

## DC Controller

<div class="product-list">

  <a href="KR1201A/QIACHIP_KR1201A/">
    <img src="KR1201A/QIACHIP_KR1201A_Product_Diagram.webp" alt="KR1201A Product Image">
    <h2>KR1201A</h2>
    
  </a>

  <a href="KR2402A/QIACHIP_KR2402A/">
    <img src="KR2402A/QIACHIP_KR2402A_Product_Diagram.webp" alt="KR2402A Product Image">
    <h2>KR2402A</h2>
    
  </a>

</div>

## AC Controller

<div class="product-list">

  <a href="KR2202/QIACHIP_KR2202/">
    <img src="KR2202/QIACHIP_KR2202_Product_Display_Figure.webp" alt="KR2202 Product Image">
    <h2>KR2202</h2>
    
  </a>

</div>