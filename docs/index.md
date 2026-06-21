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

  <a href="KR1201/KR1201A/QIACHIP_KR1201A/">
    <img src="KR1201/KR1201A/QIACHIP_KR1201A_Product_Diagram.webp" alt="KR1201A Product Image">
    <h2>KR1201A</h2>
    
  </a>

  <a href="KR1201/KR1201C/QIACHIP_KR1201C/">
    <img src="KR1201/KR1201C/QIACHIP_KR1201C_Product_Diagram.webp" alt="KR1201C Product Image">
    <h2>KR1201C</h2>
    
  </a>

  <a href="KR1201/KR1201MINI-V03/QIACHIP_KR1201MINI-V03/">
    <img src="KR1201/KR1201MINI-V03/QIACHIP_KR1201MINI-V03_Product_Diagram.webp" alt="KR1201MINI-V03 Product Image">
    <h2>KR1201MINI-V03</h2>
    
  </a>

  <a href="KR3001A/QIACHIP_KR3001A/">
    <img src="KR3001A/KR3001A_Product_Diagram.webp" alt="KR3001A Product Image">
    <h2>KR3001A</h2>
    
  </a>

  <a href="KR1202/KR1202-30R/QIACHIP_KR1202-30R/">
    <img src="KR1202/KR1202-30R/QIACHIP_KR1202-30R_Product_Diagram.webp" alt="KR1202-30R Product Image">
    <h2>KR1202-30R</h2>
    
  </a>

  <a href="KR1202/KR1202-V05/QIACHIP_KR1202-V05/">
    <img src="KR1202/KR1202-V05/QIACHIP_KR1202-V05_Product_Diagram.webp" alt="KR1202-V05 Product Image">
    <h2>KR1202-V05</h2>
    
  </a>

  <a href="KR1204/KR1204/QIACHIP_KR1204/">
    <img src="KR1204/KR1204/KR1204_Product_Diagram.webp" alt="KR1204 Product Image">
    <h2>KR1204</h2>
    
  </a>

  <a href="KR1204/KR1204B/QIACHIP_KR1204B/">
    <img src="KR1204/KR1204B/QIACHIP_KR1204B_Product_Diagram.webp" alt="KR1204B Product Image">
    <h2>KR1204B</h2>
    
  </a>

  <a href="KR2401/KR2401FB/QIACHIP_KR2401FB/">
    <img src="KR2401/KR2401FB/QIACHIP_KR2401FB_Product_Diagram.webp" alt="KR2401FB Product Image">
    <h2>KR2401FB</h2>
    
  </a>

  <a href="KR2401/KR2401F-4/QIACHIP_KR2401F-4/">
    <img src="KR2401/KR2401F-4/QIACHIP_KR2401F-4_Product_Diagram.webp" alt="KR2401F-4 Product Image">
    <h2>KR2401F-4</h2>
    
  </a>

  <a href="KR2402A/QIACHIP_KR2402A/">
    <img src="KR2402A/QIACHIP_KR2402A_Product_Diagram.webp" alt="KR2402A Product Image">
    <h2>KR2402A</h2>
    
  </a>

  <a href="KR0548/KR0548-1CH/QIACHIP_KR0548-1CH/">
    <img src="KR0548/KR0548-1CH/QIACHIP_KR0548-1CH_Product_Diagram.webp" alt="KR0548-1CH Product Image">
    <h2>KR0548-1CH</h2>
    
  </a>

  <a href="KR0548/KR0548-2CH/QIACHIP_KR0548-2CH/">
    <img src="KR0548/KR0548-2CH/QIACHIP_KR0548-2CH_Product_Diagram.webp" alt="KR0548-2CH Product Image">
    <h2>KR0548-2CH</h2>
    
  </a>

  <a href="KR0548/KR0548-4CH/QIACHIP_KR0548-4CH/">
    <img src="KR0548/KR0548-4CH/QIACHIP_KR0548-4CH_Product_Diagram.webp" alt="KR0548-4CH Product Image">
    <h2>KR0548-4CH</h2>
    
  </a>

  <a href="KR7001/QIACHIP_KR7001/">
    <img src="KR7001/QIACHIP_KR7001_Product_Diagram.webp" alt="KR7001 Product Image">
    <h2>KR7001</h2>
    
  </a>

</div>

## AC Controller

<div class="product-list">

  <a href="KR2201/KR2201-4/QIACHIP_KR2201-4/">
    <img src="KR2201/KR2201-4/QIACHIP_KR2201-4_Product_Diagram.webp" alt="KR2201-4 Product Image">
    <h2>KR2201-4</h2>
    
  </a>

  <a href="KR2201/KR2201-COM/QIACHIP_KR2201-COM/">
    <img src="KR2201/KR2201-COM/QIACHIP_KR2201-COM_Product_Diagram.webp" alt="KR2201-COM Product Image">
    <h2>KR2201-COM</h2>
    
  </a>

  <a href="KR2201/KR2201B-4/QIACHIP_KR2201B-4/">
    <img src="KR2201/KR2201B-4/QIACHIP_KR2201B-4_Product_Diagram.webp" alt="KR2201B-4 Product Image">
    <h2>KR2201B-4</h2>
    
  </a>

  <a href="KR2201/KR2201BL-4/QIACHIP_KR2201BL-4/">
    <img src="KR2201/KR2201BL-4/QIACHIP_KR2201BL-4_Product_Diagram.webp" alt="KR2201BL-4 Product Image">
    <h2>KR2201BL-4</h2>
    
  </a>

  <a href="KR2201/KR2201BY/QIACHIP_KR2201BY/">
    <img src="KR2201/KR2201BY/QIACHIP_KR2201BY_Product_Diagram.webp" alt="KR2201BY Product Image">
    <h2>KR2201BY</h2>
    
  </a>

  <a href="KR2201/KR2201DA-4/QIACHIP_KR2201DA-4/">
    <img src="KR2201/KR2201DA-4/QIACHIP_KR2201DA-4_Product_Diagram.webp" alt="KR2201DA-4 Product Image">
    <h2>KR2201DA-4</h2>
    
  </a>

  <a href="KR2201/KR2201F-4/QIACHIP_KR2201F-4/">
    <img src="KR2201/KR2201F-4/QIACHIP_KR2201F-4_Product_Diagram.webp" alt="KR2201F-4 Product Image">
    <h2>KR2201F-4</h2>
    
  </a>

  <a href="KR2201/KR2201G-4/QIACHIP_KR2201G-4/">
    <img src="KR2201/KR2201G-4/QIACHIP_KR2201G-4_Product_Diagram.webp" alt="KR2201G-4 Product Image">
    <h2>KR2201G-4</h2>
    
  </a>

  <a href="KR2201/KR2201GS-4/QIACHIP_KR2201GS-4/">
    <img src="KR2201/KR2201GS-4/QIACHIP_KR2201GS-4_Product_Diagram.webp" alt="KR2201GS-4 Product Image">
    <h2>KR2201GS-4</h2>
    
  </a>

  <a href="KR2201/KR2201W-4/QIACHIP_KR2201W-4/">
    <img src="KR2201/KR2201W-4/QIACHIP_KR2201W-4_Product_Diagram.webp" alt="KR2201W-4 Product Image">
    <h2>KR2201W-4</h2>
    
  </a>

  <a href="KR2201/KR2201WB/QIACHIP_KR2201WB/">
    <img src="KR2201/KR2201WB/QIACHIP_KR2201WB_Product_Diagram.webp" alt="KR2201WB Product Image">
    <h2>KR2201WB</h2>
    
  </a>

  <a href="KR2202/QIACHIP_KR2202/">
    <img src="KR2202/QIACHIP_KR2202_Product_Diagram.webp" alt="KR2202 Product Image">
    <h2>KR2202</h2>
    
  </a>

  <a href="KR2204/QIACHIP_KR2204/">
    <img src="KR2204/QIACHIP_KR2204_Product_Diagram.webp" alt="KR2204 Product Image">
    <h2>KR2204</h2>
    
  </a>

  <a href="KR2301/KR2301/QIACHIP_KR2301/">
    <img src="KR2301/KR2301/QIACHIP_KR2301_Product_Diagram.webp" alt="KR2301 Product Image">
    <h2>KR2301</h2>
    
  </a>

  <a href="KR2301/KR2301MT/QIACHIP_KR2301MT/">
    <img src="KR2301/KR2301MT/QIACHIP_KR2301MT_Product_Diagram.webp" alt="KR2301MT Product Image">
    <h2>KR2301MT</h2>
    
  </a>

  <a href="KR2303/QIACHIP_KR2303/">
    <img src="KR2303/QIACHIP_KR2303_Product_Diagram.webp" alt="KR2303 Product Image">
    <h2>KR2303</h2>
    
  </a>

  <a href="KR2305/QIACHIP_KR2305/">
    <img src="KR2305/QIACHIP_KR2305_Product_Diagram.webp" alt="KR2305 Product Image">
    <h2>KR2305</h2>
    
  </a>

  <a href="KR2306EW/QIACHIP_KR2306EW/">
    <img src="KR2306EW/QIACHIP_KR2306EW_Product_Diagram.webp" alt="KR2306EW Product Image">
    <h2>KR2306EW</h2>
    
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

  <a href="RX480E/RX480E-4A/QIACHIP_RX480E-4A/">
    <img src="RX480E/RX480E-4A/QIACHIP_RX480E-4A_Product_Diagram.webp" alt="RX480E-4A Product Image">
    <h2>RX480E-4A</h2>
    
  </a>

  <a href="RX480E/RX480E-4C/QIACHIP_RX480E-4C/">
    <img src="RX480E/RX480E-4C/QIACHIP_RX480E-4C_Product_Diagram.webp" alt="RX480E-4C Product Image">
    <h2>RX480E-4C</h2>
    
  </a>

  <a href="RX480E/RX480E-1A/QIACHIP_RX480E-1A/">
    <img src="RX480E/RX480E-1A/QIACHIP_RX480E-1A_Product_Diagram.webp" alt="RX480E-1A Product Image">
    <h2>RX480E-1A</h2>
    
  </a>

  <a href="RX480E/RX480E-868/QIACHIP_RX480E-868/">
    <img src="RX480E/RX480E-868/QIACHIP_RX480E-868_Product_Diagram.webp" alt="RX480E-868 Product Image">
    <h2>RX480E-868</h2>
    
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

  <a href="MTD12A-4/QIACHIP_MTD12A-4/">
    <img src="MTD12A-4/QIACHIP_MTD12A-4_Product_Diagram.webp" alt="MTD12A-4 Product Image">
    <h2>MTD12A-4</h2>
    
  </a>

  <a href="RX500-4/QIACHIP_RX500-4/">
    <img src="RX500-4/QIACHIP_RX500-4_Product_Diagram.webp" alt="RX500-4 Product Image">
    <h2>RX500-4</h2>
    
  </a>

  <a href="RX470-4/QIACHIP_RX470-4/">
    <img src="RX470-4/QIACHIP_RX470-4_Product_Diagram.webp" alt="RX470-4 Product Image">
    <h2>RX470-4</h2>
    
  </a>

  <a href="RX217E-V01/QIACHIP_RX217E-V01/">
    <img src="RX217E-V01/QIACHIP_RX217E-V01_Product_Diagram.webp" alt="RX217E-V01 Product Image">
    <h2>RX217E-V01</h2>
    
  </a>

  <a href="WL101-341/QIACHIP_WL101-341/">
    <img src="WL101-341/QIACHIP_WL101-341_Product_Diagram.webp" alt="WL101-341 Product Image">
    <h2>WL101-341</h2>
    
  </a>

  <a href="RX18210A-4/QIACHIP_RX18210A-4/">
    <img src="RX18210A-4/QIACHIP_RX18210A-4_Product_Diagram.webp" alt="RX18210A-4 Product Image">
    <h2>RX18210A-4</h2>
    
  </a>

  <a href="RX18211A-4/QIACHIP_RX18211A-4/">
    <img src="RX18211A-4/QIACHIP_RX18211A-4_Product_Diagram.webp" alt="RX18211A-4 Product Image">
    <h2>RX18211A-4</h2>
    
  </a>

</div>

## Wireless Transmitter Module

<div class="product-list">

  <a href="WL102-341/QIACHIP_WL102-341/">
    <img src="WL102-341/QIACHIP_WL102_Product_Diagram.webp" alt="WL102-341 Product Image">
    <h2>WL102-341</h2>
    
  </a>

  <a href="TX118SA-4/QIACHIP_TX118SA-4/">
    <img src="TX118SA-4/QIACHIP_TX118SA-4_Product_Diagram.webp" alt="TX118SA-4 Product Image">
    <h2>TX118SA-4</h2>
    
  </a>

  <a href="TX181-4/QIACHIP_TX181-4/">
    <img src="TX181-4/QIACHIP_TX181-4_Product_Diagram.webp" alt="TX181-4 Product Image">
    <h2>TX181-4</h2>
    
  </a>

</div>