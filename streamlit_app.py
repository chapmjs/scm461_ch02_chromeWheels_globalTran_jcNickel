import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Little's Law Homework",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# HELPER FUNCTIONS (Little's Law)
# ============================================================================

def littles_law_I(R, T):
    """Calculate Inventory: I = R × T"""
    return R * T

def littles_law_R(I, T):
    """Calculate Throughput: R = I / T"""
    return I / T if T != 0 else 0

def littles_law_T(I, R):
    """Calculate Flow Time: T = I / R"""
    return I / R if R != 0 else 0

# ============================================================================
# CALCULATIONS
# ============================================================================

# TODO: Replace these with your calculated values from the homework template

# PROBLEM 4: CHROME WHEELS
cw_total_inventory = 192.0  # TODO: Calculate using Little's Law
cw_standard_inventory = 174.0  # TODO: Calculate
cw_standard_flow_time = 8.7  # TODO: Calculate
cw_ex_chrome_flow_time = 2.0  # TODO: Calculate
cw_ultra_flow_time = 1.25  # TODO: Calculate

# PROBLEM 5: GLOBAL TRANS
gt_throughput_per_day = 3.0  # TODO: Calculate
gt_monthly_earnings = 4500000.0  # TODO: Calculate
gt_travel_time = 8.0  # TODO: Calculate
gt_total_cycle_time = 10.0  # TODO: Calculate

# PROBLEM 6: J.C. NICKEL
jc_cashier_wait_time = 6.0  # TODO: Calculate
jc_fraction_self_checkout = 0.5  # TODO: Calculate
jc_self_checkout_service_time = 4.0  # TODO: Calculate
jc_self_checkout_wait_time = 1.0  # TODO: Calculate
jc_avg_total_checkout_time = 7.0  # TODO: Calculate
jc_cashier_throughput = 60.0  # TODO: Calculate
jc_self_checkout_throughput = 60.0  # TODO: Calculate
jc_new_scenario_wait = 2.14  # TODO: Calculate (with 8 cashiers)
jc_required_queue_for_2min = 4.7  # TODO: Calculate

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Operations_research_icon.svg/240px-Operations_research_icon.svg.png", 
             width=100)
    st.header("📚 Little's Law")
    
    st.latex(r"I = R \times T")
    
    st.markdown("""
    **Where:**
    - **I** = Inventory (units in system)
    - **R** = Throughput Rate (units/time)
    - **T** = Flow Time (time/unit)
    
    ---
    
    **Key Insight:** 
    This fundamental relationship holds for any stable system in steady state!
    
    ---
    
    **Applications in this homework:**
    1. 🔧 Manufacturing (Chrome Wheels)
    2. 🚢 Logistics (Global Trans)
    3. 🛒 Retail Operations (J.C. Nickel)
    """)
    
    st.markdown("---")
    st.caption("Operations Management Homework | Spring 2025")

# ============================================================================
# MAIN TITLE
# ============================================================================

st.title("📊 Little's Law in Operations Management")
st.markdown("### Application of I = R × T to Real-World Problems")
st.markdown("**Student:** [Your Name Here] | **Date:** [Date]")
st.markdown("---")

# ============================================================================
# PROBLEM 4: CHROME WHEELS INC.
# ============================================================================

st.header("🔧 Problem 4: Chrome Wheels Inc.")
st.markdown("*Manufacturing with Priority Systems*")

with st.expander("📋 View Problem Statement", expanded=False):
    st.markdown("""
    Chrome Wheels (CW) Inc. makes custom gear alloy wheels with three priority levels:
    
    | Order Type | Priority | Arrival Rate | Avg Outstanding |
    |------------|----------|--------------|-----------------|
    | **Ultra-chrome** | Highest (1) | 8 orders/day | 10 orders |
    | **Ex-chrome** | Medium (2) | 4 orders/day | 8 orders |
    | **Standard** | Lowest (3) | 20 orders/day | ??? |
    
    **Given Information:**
    - Average production time for any order: **6 days**
    - Orders are processed by priority
    - Once finished, orders ship same day
    
    **Questions:**
    1. What is the total average number of outstanding orders?
    2. What is the average waiting time for standard wheel customers?
    3. What is the average waiting time for ex-chrome and ultra-chrome customers?
    """)

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Inventory",
        value=f"{cw_total_inventory:.0f} orders",
        help="Total outstanding orders across all types"
    )

with col2:
    st.metric(
        label="Standard Inventory",
        value=f"{cw_standard_inventory:.0f} orders",
        help="Outstanding standard orders"
    )

with col3:
    st.metric(
        label="Standard Wait Time",
        value=f"{cw_standard_flow_time:.1f} days",
        delta=f"{cw_standard_flow_time - 6:.1f} vs system avg",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="Priority Wait Time",
        value=f"~{(cw_ex_chrome_flow_time + cw_ultra_flow_time)/2:.1f} days",
        delta=f"{((cw_ex_chrome_flow_time + cw_ultra_flow_time)/2) - 6:.1f} vs system avg",
        delta_color="normal"
    )

# Visualization 1: Inventory Distribution
st.subheader("📦 Inventory Distribution by Priority Level")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    inventory_data = pd.DataFrame({
        'Order Type': ['Ultra-chrome', 'Ex-chrome', 'Standard'],
        'Average Inventory': [10, 8, cw_standard_inventory],
        'Priority': [1, 2, 3]
    })
    
    fig_inventory = px.bar(
        inventory_data, 
        x='Order Type', 
        y='Average Inventory',
        color='Priority',
        color_continuous_scale='RdYlGn_r',
        title='Average Outstanding Orders by Type',
        text='Average Inventory'
    )
    fig_inventory.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig_inventory.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_inventory, use_container_width=True)

with col_chart2:
    flow_time_data = pd.DataFrame({
        'Order Type': ['Ultra-chrome', 'Ex-chrome', 'Standard', 'System Average'],
        'Flow Time (days)': [cw_ultra_flow_time, cw_ex_chrome_flow_time, 
                             cw_standard_flow_time, 6.0],
        'Category': ['Priority', 'Priority', 'Standard', 'Average']
    })
    
    fig_flow = px.bar(
        flow_time_data,
        x='Order Type',
        y='Flow Time (days)',
        color='Category',
        color_discrete_map={'Priority': '#4ECDC4', 'Standard': '#FF6B6B', 'Average': '#95E1D3'},
        title='Customer Waiting Time Comparison',
        text='Flow Time (days)'
    )
    fig_flow.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_flow.update_layout(height=400)
    st.plotly_chart(fig_flow, use_container_width=True)

# Key Insights
st.info("""
**📌 Key Insights:**
- Higher priority orders experience significantly shorter wait times
- Standard orders bear the burden of the priority system
- Total inventory is distributed heavily toward lower-priority items
- System average of 6 days masks the inequality in wait times
""")

st.markdown("---")

# ============================================================================
# PROBLEM 5: GLOBAL TRANS CO.
# ============================================================================

st.header("🚢 Problem 5: Global Trans Co.")
st.markdown("*Logistics and Transportation Systems*")

with st.expander("📋 View Problem Statement", expanded=False):
    st.markdown("""
    Global Trans Co. operates a fleet of ships delivering goods in Europe.
    
    **Given Information:**
    - **Total fleet:** 30 ships
    - **Average ships in port (France):** 6 ships
    - **Average time in port:** 2 days
    - **Revenue per delivery:** $50,000
    
    **Questions:**
    1. What is the monthly earning of the firm? (assume 30 days/month)
    2. What is the average travel time for ships? (time from leaving port until returning)
    """)

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Monthly Earnings",
        value=f"${gt_monthly_earnings:,.0f}",
        help="Total revenue for 30 days"
    )

with col2:
    st.metric(
        label="Daily Throughput",
        value=f"{gt_throughput_per_day:.1f} ships",
        help="Deliveries completed per day"
    )

with col3:
    st.metric(
        label="Travel Time",
        value=f"{gt_travel_time:.1f} days",
        help="Average time at sea per round trip"
    )

with col4:
    st.metric(
        label="Total Cycle Time",
        value=f"{gt_total_cycle_time:.1f} days",
        help="Port time + travel time"
    )

# Visualization: Ship Flow System
st.subheader("🔄 Ship Flow Dynamics")

col_sys1, col_sys2 = st.columns(2)

with col_sys1:
    # Gauge for throughput
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=gt_throughput_per_day,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Daily Throughput", 'font': {'size': 20}},
        delta={'reference': 2.5, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 5], 'tickwidth': 1},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 2], 'color': '#FFE5E5'},
                {'range': [2, 4], 'color': '#FFF8DC'},
                {'range': [4, 5], 'color': '#E5FFE5'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 3
            }
        }
    ))
    fig_gauge.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_sys2:
    # System breakdown
    cycle_data = pd.DataFrame({
        'Phase': ['At Port', 'Traveling'],
        'Time (days)': [2, gt_travel_time],
        'Ships': [6, 24]
    })
    
    fig_cycle = px.pie(
        cycle_data,
        values='Time (days)',
        names='Phase',
        title='Time Distribution per Cycle',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4'],
        hole=0.4
    )
    fig_cycle.update_traces(textposition='inside', textinfo='label+percent')
    fig_cycle.update_layout(height=300)
    st.plotly_chart(fig_cycle, use_container_width=True)

# Sankey Diagram
st.subheader("📊 Ship Flow Visualization")

fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["🏴󠁧󠁢󠁥󠁮󠁧󠁿 Port (6 ships)", "🌊 At Sea (24 ships)", "✅ Deliveries (3/day)"],
        color=["#3498db", "#2ecc71", "#f39c12"],
        x=[0.1, 0.5, 0.9],
        y=[0.5, 0.5, 0.5]
    ),
    link=dict(
        source=[0, 1],
        target=[1, 2],
        value=[gt_throughput_per_day, gt_throughput_per_day],
        color=["rgba(52, 152, 219, 0.4)", "rgba(46, 204, 113, 0.4)"]
    )
)])

fig_sankey.update_layout(
    title="Daily Ship Flow (ships per day)",
    font_size=14,
    height=250,
    margin=dict(l=20, r=20, t=50, b=20)
)
st.plotly_chart(fig_sankey, use_container_width=True)

# Revenue calculation breakdown
with st.expander("💰 Revenue Calculation Breakdown"):
    st.latex(r"\text{Monthly Earnings} = \text{Throughput} \times \text{Revenue per Delivery} \times \text{Days}")
    st.latex(f"= {gt_throughput_per_day:.1f} \\text{{ ships/day}} \\times \\$50,000 \\times 30 \\text{{ days}}")
    st.latex(f"= \\${gt_monthly_earnings:,.0f}")

st.markdown("---")

# ============================================================================
# PROBLEM 6: J.C. NICKEL RETAIL STORE
# ============================================================================

st.header("🛒 Problem 6: J.C. Nickel Retail Store")
st.markdown("*Multi-Server Queuing Systems*")

with st.expander("📋 View Problem Statement", expanded=False):
    st.markdown("""
    J.C. Nickel is a retail store with two checkout options:
    
    **System Configuration:**
    - **Cashiers:** 6 cashiers (1 idle on average)
    - **Self-Checkout:** 2 machines (1 idle on average)
    - **Total customers:** 120 per hour
    
    **Observed Data:**
    - Cashier service time: 3 minutes per customer
    - Customers waiting for cashiers: 10 (average)
    - Self-checkout total time: 5 minutes (wait + service)
    
    **Questions:**
    1. Expected waiting time in cashier line?
    2. Fraction of customers using self-checkout?
    3. Average time using a self-checkout machine (service only)?
    4. Average checkout time across all customers?
    5. Evaluate: "2 more cashiers → half the line → wait time < 2 min"
    """)

# Key Metrics Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Cashier Wait Time",
        value=f"{jc_cashier_wait_time:.1f} min",
        help="Time in line before reaching cashier"
    )

with col2:
    st.metric(
        label="Self-Checkout Usage",
        value=f"{jc_fraction_self_checkout:.0%}",
        help="Fraction of customers using self-checkout"
    )

with col3:
    st.metric(
        label="Self-Checkout Service",
        value=f"{jc_self_checkout_service_time:.1f} min",
        help="Time actually using the machine"
    )

with col4:
    st.metric(
        label="Average Total Time",
        value=f"{jc_avg_total_checkout_time:.1f} min",
        help="Weighted average across all customers"
    )

# Customer Flow Distribution
st.subheader("👥 Customer Flow Analysis")

col_flow1, col_flow2 = st.columns(2)

with col_flow1:
    customer_split = pd.DataFrame({
        'Checkout Type': ['Cashiers', 'Self-Checkout'],
        'Customers per Hour': [jc_cashier_throughput, jc_self_checkout_throughput]
    })
    
    fig_split = px.pie(
        customer_split,
        values='Customers per Hour',
        names='Checkout Type',
        title='Customer Distribution (120 customers/hour)',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4'],
        hole=0.5
    )
    fig_split.update_traces(textposition='inside', textinfo='label+value+percent')
    fig_split.update_layout(height=350)
    st.plotly_chart(fig_split, use_container_width=True)

with col_flow2:
    time_comparison = pd.DataFrame({
        'Checkout Type': ['Cashier\n(Wait)', 'Cashier\n(Service)', 
                         'Self-Checkout\n(Wait)', 'Self-Checkout\n(Service)'],
        'Time (minutes)': [jc_cashier_wait_time, 3.0, 
                          jc_self_checkout_wait_time, jc_self_checkout_service_time],
        'Component': ['Wait', 'Service', 'Wait', 'Service']
    })
    
    fig_time_comp = px.bar(
        time_comparison,
        x='Checkout Type',
        y='Time (minutes)',
        color='Component',
        title='Time Breakdown by Checkout Type',
        text='Time (minutes)',
        color_discrete_map={'Wait': '#FFD93D', 'Service': '#6BCB77'}
    )
    fig_time_comp.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    fig_time_comp.update_layout(height=350, showlegend=True)
    st.plotly_chart(fig_time_comp, use_container_width=True)

# Scenario Analysis
st.subheader("💡 Scenario Analysis: Adding 2 More Cashiers")

col_scenario = st.columns([2, 1])

with col_scenario[0]:
    scenario_comparison = pd.DataFrame({
        'Scenario': ['Current\n(6 cashiers)', 'Proposed\n(8 cashiers)'],
        'Queue Length': [10, 5],
        'Wait Time (min)': [jc_cashier_wait_time, jc_new_scenario_wait],
        'Busy Cashiers': [5, 7]
    })
    
    fig_scenario = go.Figure()
    
    # Add bars for queue length
    fig_scenario.add_trace(go.Bar(
        name='Queue Length',
        x=scenario_comparison['Scenario'],
        y=scenario_comparison['Queue Length'],
        yaxis='y',
        marker_color='#FF6B6B',
        text=scenario_comparison['Queue Length'],
        textposition='outside'
    ))
    
    # Add line for wait time
    fig_scenario.add_trace(go.Scatter(
        name='Wait Time (min)',
        x=scenario_comparison['Scenario'],
        y=scenario_comparison['Wait Time (min)'],
        yaxis='y2',
        mode='lines+markers+text',
        marker=dict(size=12, color='#4ECDC4'),
        line=dict(width=3),
        text=scenario_comparison['Wait Time (min)'].round(2),
        textposition='top center'
    ))
    
    # Add target line
    fig_scenario.add_hline(
        y=2, line_dash="dash", line_color="green",
        annotation_text="Target: 2 min",
        yaxis='y2'
    )
    
    fig_scenario.update_layout(
        title='Impact of Adding 2 Cashiers',
        yaxis=dict(title='Queue Length (customers)', titlefont=dict(color='#FF6B6B')),
        yaxis2=dict(
            title='Wait Time (minutes)',
            titlefont=dict(color='#4ECDC4'),
            overlaying='y',
            side='right',
            range=[0, 8]
        ),
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig_scenario, use_container_width=True)

with col_scenario[1]:
    st.markdown("#### Evaluation")
    st.markdown("**Claim:** *'Adding 2 cashiers will cut the line in half and reduce wait to <2 min'*")
    
    # Check 1: Queue reduction
    if 5 == 10 / 2:
        st.success("✅ Queue: IF cut to half (assumed)")
    else:
        st.warning("⚠️ Queue reduction not guaranteed")
    
    # Check 2: Wait time
    if jc_new_scenario_wait < 2:
        st.success(f"✅ Wait: {jc_new_scenario_wait:.2f} min < 2 min")
    else:
        st.error(f"❌ Wait: {jc_new_scenario_wait:.2f} min ≥ 2 min")
    
    st.markdown("---")
    st.info(f"""
    **Reality Check:**
    
    To achieve 2-minute wait, queue must be ≤ {jc_required_queue_for_2min:.1f} customers.
    
    Adding cashiers increases throughput but doesn't automatically cut queue in half.
    """)

# Detailed breakdown
with st.expander("🔍 Detailed Little's Law Applications"):
    st.markdown("""
    ### Problem 6 uses Little's Law multiple times:
    
    **1. Cashier System:**
    - Queue: I = 10 customers, R = 5/3 cust/min → T = 6 min wait
    - Total: Wait (6 min) + Service (3 min) = 9 min
    
    **2. Self-Checkout System:**
    - Total: I = R × T, with T = 5 min total
    - Can decompose into wait + service
    
    **3. Overall System:**
    - Weighted average based on customer split
    """)

st.markdown("---")

# ============================================================================
# SUMMARY AND INSIGHTS
# ============================================================================

st.header("📈 Summary: Little's Law Across Three Domains")

tab1, tab2, tab3 = st.tabs(["🎯 Key Insights", "📊 Comparative Analysis", "🧮 Formulas Used"])

with tab1:
    col_insight1, col_insight2 = st.columns(2)
    
    with col_insight1:
        st.markdown("""
        ### 🔧 Manufacturing (Chrome Wheels)
        
        **Lesson:** Priority systems create unequal experiences
        - Higher priority → Lower inventory → Shorter wait
        - Standard customers wait 7x longer than ultra customers
        - System average (6 days) masks this inequality
        
        **Little's Law Application:**
        - Total system: I = R × T
        - By priority level: decompose inventory
        """)
        
        st.markdown("""
        ### 🚢 Logistics (Global Trans)
        
        **Lesson:** System capacity is the constraint
        - 30 ships but only 3 deliveries/day
        - Most time spent traveling (80%)
        - Increasing port efficiency alone won't help much
        
        **Little's Law Application:**
        - Port subsystem: I = 6, T = 2 → R = 3
        - Total system: I = 30, R = 3 → T = 10
        """)
    
    with col_insight2:
        st.markdown("""
        ### 🛒 Retail (J.C. Nickel)
        
        **Lesson:** Multi-server systems need careful analysis
        - Self-checkout faster but lower capacity utilization
        - Adding servers ≠ proportional improvement
        - Queue dynamics are non-linear
        
        **Little's Law Application:**
        - Separate analysis for each subsystem
        - Queue vs. total system
        - Scenario comparison
        """)
        
        st.success("""
        ### 🎓 Universal Principle
        
        **Little's Law (I = R × T) works because:**
        - It's conservation of flow
        - No assumptions about distributions
        - Only requires steady state
        - Applies to subsystems and total system
        """)

with tab2:
    comparison_data = pd.DataFrame({
        'Problem': ['Chrome Wheels', 'Global Trans', 'J.C. Nickel'],
        'Industry': ['Manufacturing', 'Logistics', 'Retail'],
        'Avg Inventory': [192, 30, 11],
        'Throughput (per period)': [32, 3, 120],
        'Avg Flow Time (periods)': [6, 10, 0.092],  # 5.5 min in hours
        'Key Challenge': ['Priority management', 'Capacity constraint', 'Queue management']
    })
    
    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("""
    **Observations:**
    - All three use the same fundamental law (I = R × T)
    - But apply it to different operational contexts
    - Manufacturing: managing priority levels
    - Logistics: understanding system capacity
    - Retail: optimizing multiple server systems
    """)

with tab3:
    st.markdown("""
    ### Little's Law Formula and Rearrangements
    """)
    
    col_form1, col_form2, col_form3 = st.columns(3)
    
    with col_form1:
        st.markdown("**Standard Form:**")
        st.latex(r"I = R \times T")
        st.markdown("*Inventory = Throughput × Flow Time*")
    
    with col_form2:
        st.markdown("**Solve for Throughput:**")
        st.latex(r"R = \frac{I}{T}")
        st.markdown("*Throughput = Inventory / Flow Time*")
    
    with col_form3:
        st.markdown("**Solve for Flow Time:**")
        st.latex(r"T = \frac{I}{R}")
        st.markdown("*Flow Time = Inventory / Throughput*")
    
    st.markdown("---")
    
    st.markdown("### Applications in Each Problem")
    
    st.markdown("""
    **Problem 4 (Chrome Wheels):**
    - Used I = R × T to find total inventory
    - Used T = I / R to find flow times by priority
    
    **Problem 5 (Global Trans):**
    - Used R = I / T at the port (I=6, T=2)
    - Used T = I / R for total cycle (I=30, R=3)
    
    **Problem 6 (J.C. Nickel):**
    - Used R = (busy servers) / (service time) for throughput
    - Used T = I / R for waiting times
    - Applied to multiple subsystems
    """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Operations Management Homework</strong></p>
    <p>Little's Law Application | I = R × T</p>
    <p>🔧 Manufacturing • 🚢 Logistics • 🛒 Retail</p>
</div>
""", unsafe_allow_html=True)

# Optional: Add data download
with st.expander("📥 Download Results Data"):
    results_df = pd.DataFrame({
        'Problem': ['Chrome Wheels', 'Chrome Wheels', 'Chrome Wheels',
                   'Global Trans', 'Global Trans',
                   'J.C. Nickel', 'J.C. Nickel', 'J.C. Nickel'],
        'Metric': ['Total Inventory', 'Standard Flow Time', 'Ultra Flow Time',
                  'Monthly Earnings', 'Travel Time',
                  'Cashier Wait', 'Self-Checkout %', 'Avg Total Time'],
        'Value': [cw_total_inventory, cw_standard_flow_time, cw_ultra_flow_time,
                 gt_monthly_earnings, gt_travel_time,
                 jc_cashier_wait_time, jc_fraction_self_checkout, jc_avg_total_checkout_time],
        'Units': ['orders', 'days', 'days', 'dollars', 'days', 
                 'minutes', 'fraction', 'minutes']
    })
    
    st.dataframe(results_df, use_container_width=True, hide_index=True)
    
    csv = results_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name='littles_law_homework_results.csv',
        mime='text/csv',
    )
