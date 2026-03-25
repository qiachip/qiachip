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

  <a href="KR1204/QIACHIP_KR1204/">
    <img src="KR1204/KR1204_Product_Diagram.webp" alt="KR1204 Product Image">
    <h2>KR1204</h2>
    
  </a>

  <a href="KR1204B/QIACHIP_KR1204B/">
    <img src="KR1204B/QIACHIP_KR1204B_Product_Diagram.webp" alt="KR1204B Product Image">
    <h2>KR1204B</h2>
    
  </a>

  <a href="KR2401FB/QIACHIP_KR2401FB/">
    <img src="KR2401FB/QIACHIP_KR2401FB_Product_Diagram.webp" alt="KR2401FB Product Image">
    <h2>KR2401FB</h2>
    
  </a>

  <a href="KR2402A/QIACHIP_KR2402A/">
    <img src="KR2402A/QIACHIP_KR2402A_Product_Diagram.webp" alt="KR2402A Product Image">
    <h2>KR2402A</h2>
    
  </a>

  <a href="KR3001A/QIACHIP_KR3001A/">
    <img src="KR3001A/KR3001A_Product_Diagram.webp" alt="KR3001A Product Image">
    <h2>KR3001A</h2>
    
  </a>

</div>

## AC Controller

<div class="product-list">

  <a href="KR2201-4/QIACHIP_KR2201-4/">
    <img src="KR2201-4/QIACHIP_KR2201-4_Product_Diagram.webp" alt="KR2201-4 Product Image">
    <h2>KR2201-4</h2>
    
  </a>

  <a href="KR2201-COM/QIACHIP_KR2201-COM/">
    <img src="KR2201-COM/QIACHIP_KR2201-COM_Product_Diagram.webp" alt="KR2201-COM Product Image">
    <h2>KR2201-COM</h2>
    
  </a>

  <a href="KR2202/QIACHIP_KR2202/">
    <img src="KR2202/QIACHIP_KR2202_Product_Diagram.webp" alt="KR2202 Product Image">
    <h2>KR2202</h2>
    
  </a>

  <a href="KR2204/QIACHIP_KR2204/">
    <img src="KR2204/QIACHIP_KR2204_Product_Diagram.webp" alt="KR2204 Product Image">
    <h2>KR2204</h2>
    
  </a>

  <a href="KR2201G/QIACHIP_KR2201G/">
    <img src="KR2201G/QIACHIP_KR2201G_Product_Diagram.webp" alt="KR2201G Product Image">
    <h2>KR2201G</h2>
    
  </a>

</div>

## Ceiling Fan Light Controller

<div class="product-list">

  <a href="FLC05-E110V/QIACHIP_FLC05-E110V/">
    <img src="FLC05-E110V/QIACHIP_FLC05-110V_Product_Diagram.webp" alt="FLC05-E110V Product Image">
    <h2>FLC05-E110V</h2>
    
  </a>

  <a href="FLC05-E220V/QIACHIP_FLC05-E220V/">
    <img src="FLC05-E220V/QIACHIP_FLC05-220V_Product_Diagram.webp" alt="FLC05-E220V Product Image">
    <h2>FLC05-E220V</h2>
    
  </a>

</div>

## Wireless Receiver Module

<div class="product-list">

  <a href="RX470-4/QIACHIP_RX470-4/">
    <img src="RX470-4/QIACHIP_RX470-4_Product_Diagram.webp" alt="RX470-4 Product Image">
    <h2>RX470-4</h2>
    
  </a>

  <a href="QA-R-011/QIACHIP_QA-R-011/">
    <img src="QA-R-011/QIACHIP_QA-R-011_Product_Diagram.webp" alt="QA-R-011 Product Image">
    <h2>QA-R-011</h2>
    
  </a>

  <a href="QA-R-012/QIACHIP_QA-R-012/">
    <img src="QA-R-012/QIACHIP_QA-R-012_Product_Diagram.webp" alt="QA-R-012 Product Image">
    <h2>QA-R-012</h2>
    
  </a>

  <a href="QA-R-012V3/QIACHIP_QA-R-012V3/">
    <img src="QA-R-012V3/QIACHIP_QA-R-012V3_Product_Diagram.webp" alt="QA-R-012V3 Product Image">
    <h2>QA-R-012V3</h2>
    
  </a>

</div>

## Wireless Transmitter Module

<div class="product-list">

  <a href="WL102-341/QIACHIP_WL102-341/">
    <img src="WL102-341/QIACHIP_WL102_Product_Diagram.webp" alt="WL102-341 Product Image">
    <h2>WL102-341</h2>
    
  </a>

</div>