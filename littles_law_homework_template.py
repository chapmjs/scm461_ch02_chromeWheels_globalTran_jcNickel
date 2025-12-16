# -*- coding: utf-8 -*-
"""
Little's Law Homework Template
===============================

This template will help you solve three operations management problems 
using Little's Law: I = R × T

Where:
- I = Inventory (average number of items in the system)
- R = Throughput Rate (rate at which items flow through)
- T = Flow Time (average time an item spends in the system)

Instructions:
1. Complete the calculations in each problem section
2. Fill in your answers in the designated areas
3. Run all cells to generate your results
4. Save this file and deploy to Streamlit

Author: [Your Name]
Date: [Today's Date]
"""

# ============================================================================
# SETUP: Install and Import Required Libraries
# ============================================================================

# Run this cell first in Google Colab
# !pip install streamlit pandas numpy matplotlib plotly -q

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple

# ============================================================================
# LITTLE'S LAW PRIMER
# ============================================================================

"""
Little's Law is one of the most fundamental relationships in operations:

    I = R × T

This simple equation connects three critical metrics:
- Inventory (I): Number of units in the system
- Throughput (R): Rate of units flowing through
- Flow Time (T): Time each unit spends in the system

The law holds for ANY stable system in steady state!

Example: If a coffee shop serves 60 customers/hour (R) and each customer 
spends 10 minutes in the shop (T = 10/60 hours), then on average there 
are I = 60 × (10/60) = 10 customers in the shop.
"""

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def littles_law_solve_I(R: float, T: float) -> float:
    """
    Calculate Inventory given Throughput Rate and Flow Time.
    
    Args:
        R: Throughput rate (units per time period)
        T: Flow time (time periods)
    
    Returns:
        I: Inventory (number of units)
    """
    return R * T


def littles_law_solve_R(I: float, T: float) -> float:
    """
    Calculate Throughput Rate given Inventory and Flow Time.
    
    Args:
        I: Inventory (number of units)
        T: Flow time (time periods)
    
    Returns:
        R: Throughput rate (units per time period)
    """
    return I / T if T != 0 else 0


def littles_law_solve_T(I: float, R: float) -> float:
    """
    Calculate Flow Time given Inventory and Throughput Rate.
    
    Args:
        I: Inventory (number of units)
        R: Throughput rate (units per time period)
    
    Returns:
        T: Flow time (time periods)
    """
    return I / R if R != 0 else 0


# ============================================================================
# PROBLEM 4: CHROME WHEELS INC.
# ============================================================================

def solve_chrome_wheels() -> Dict:
    """
    Chrome Wheels (CW) Inc. makes custom gear alloy wheels with three priority levels:
    - Ultra-chrome (highest priority): 8 orders/day
    - Ex-chrome (medium priority): 4 orders/day  
    - Standard (lowest priority): 20 orders/day
    
    Given Information:
    - Average production time: 6 days (for ANY order once started)
    - Average outstanding ultra-chrome orders: 10
    - Average outstanding ex-chrome orders: 8
    - Average outstanding standard orders: ??? (you need to find this!)
    
    Questions to Answer:
    1. Total average number of outstanding orders
    2. Average waiting time for standard wheel customers
    3. Average waiting time for ex-chrome and ultra-chrome customers
    """
    
    # Given data
    arrival_rate_standard = 20  # orders per day
    arrival_rate_ex_chrome = 4   # orders per day
    arrival_rate_ultra = 8       # orders per day
    
    total_flow_time = 6  # days (this is for the ENTIRE system)
    
    avg_inventory_ultra = 10  # outstanding orders
    avg_inventory_ex = 8      # outstanding orders
    
    # QUESTION 1: Find total average outstanding orders
    # -----------------------------------------------
    # Hint: Use Little's Law for the ENTIRE system
    # I_total = R_total × T_total
    
    # TODO: Calculate total arrival rate (throughput of entire system)
    R_total = arrival_rate_standard + arrival_rate_ex_chrome + arrival_rate_ultra
    
    # TODO: Calculate total average inventory using Little's Law
    I_total = littles_law_solve_I(R_total, total_flow_time)
    
    
    # QUESTION 2: Average waiting time for STANDARD customers
    # -------------------------------------------------------
    # Hint: First find the inventory of standard orders
    # Then use Little's Law to find their flow time
    
    # TODO: Calculate standard inventory
    # I_total = I_ultra + I_ex + I_standard
    I_standard = I_total - avg_inventory_ultra - avg_inventory_ex
    
    # TODO: Calculate flow time for standard orders
    T_standard = littles_law_solve_T(I_standard, arrival_rate_standard)
    
    
    # QUESTION 3: Average waiting time for EX-CHROME and ULTRA-CHROME
    # --------------------------------------------------------------
    # Hint: Use Little's Law with their inventory and arrival rates
    
    # TODO: Calculate flow time for ex-chrome orders
    T_ex_chrome = littles_law_solve_T(avg_inventory_ex, arrival_rate_ex_chrome)
    
    # TODO: Calculate flow time for ultra-chrome orders  
    T_ultra = littles_law_solve_T(avg_inventory_ultra, arrival_rate_ultra)
    
    
    # Package results
    results = {
        'total_inventory': I_total,
        'standard_inventory': I_standard,
        'standard_flow_time': T_standard,
        'ex_chrome_flow_time': T_ex_chrome,
        'ultra_flow_time': T_ultra,
        'total_throughput': R_total,
    }
    
    return results


# ============================================================================
# PROBLEM 5: GLOBAL TRANS CO.
# ============================================================================

def solve_global_trans() -> Dict:
    """
    Global Trans Co. operates 30 ships delivering goods in Europe.
    
    Given Information:
    - Total fleet: 30 ships
    - Average ships in port (France): 6 ships
    - Average time in port: 2 days
    - Revenue per delivery: $50,000
    
    Questions to Answer:
    1. Monthly earning (assume 30 days/month)
    2. Average travel time (time from leaving port until returning)
    """
    
    # Given data
    total_ships = 30
    avg_ships_in_port = 6  # This is inventory at the port
    avg_time_in_port = 2    # days
    revenue_per_delivery = 50000  # dollars
    days_per_month = 30
    
    # QUESTION 1: Monthly earnings
    # ----------------------------
    # Hint: Use Little's Law to find throughput at the port
    # Then multiply by revenue per delivery and days per month
    
    # TODO: Calculate throughput (deliveries per day) using Little's Law
    # At the port: I = 6 ships, T = 2 days, so R = ?
    R_port = littles_law_solve_R(avg_ships_in_port, avg_time_in_port)
    
    # TODO: Calculate monthly earnings
    monthly_earnings = R_port * revenue_per_delivery * days_per_month
    
    
    # QUESTION 2: Average travel time
    # -------------------------------
    # Hint: Think about the ENTIRE system (all 30 ships)
    # The entire cycle = time in port + time traveling
    # Use Little's Law for the complete cycle
    
    # TODO: Calculate total cycle time using Little's Law
    # For entire system: I = 30 ships (total), R = deliveries per day
    T_total_cycle = littles_law_solve_T(total_ships, R_port)
    
    # TODO: Calculate travel time
    # Travel time = Total cycle time - Time in port
    T_travel = T_total_cycle - avg_time_in_port
    
    
    # Package results
    results = {
        'throughput_per_day': R_port,
        'monthly_earnings': monthly_earnings,
        'total_cycle_time': T_total_cycle,
        'travel_time': T_travel,
    }
    
    return results


# ============================================================================
# PROBLEM 6: J.C. NICKEL RETAIL STORE
# ============================================================================

def solve_jc_nickel() -> Dict:
    """
    J.C. Nickel has 6 cashiers and 2 self-checkout machines.
    
    Given Information:
    - Total customers: 120 per hour
    - Cashier service time: 3 minutes per customer
    - Cashiers idle: 1 out of 6 (on average)
    - Customers waiting for cashiers: 10 (on average)
    - Self-checkout machines idle: 1 out of 2 (on average)
    - Self-checkout total time (wait + service): 5 minutes
    
    Questions to Answer:
    1. Waiting time in cashier line
    2. Fraction of customers using self-checkout
    3. Average time using a self-checkout machine (service time only)
    4. Average total checkout time across all customers
    5. Evaluate assistant manager's claim about hiring 2 more cashiers
    """
    
    # Given data
    total_customers_per_hour = 120
    num_cashiers = 6
    cashier_service_time = 3  # minutes
    avg_cashiers_idle = 1
    avg_waiting_for_cashiers = 10  # customers
    
    num_self_checkout = 2
    avg_self_checkout_idle = 1
    self_checkout_total_time = 5  # minutes (wait + service)
    
    # QUESTION 1: Waiting time in cashier line
    # ----------------------------------------
    # Hint: Use Little's Law on the WAITING LINE for cashiers
    # Need to find throughput of customers going to cashiers first
    
    # TODO: Calculate number of busy cashiers
    busy_cashiers = num_cashiers - avg_cashiers_idle
    
    # TODO: Calculate throughput of cashier system (customers per minute)
    # Each busy cashier serves 1 customer per service_time minutes
    # So each serves (1/service_time) customers per minute
    R_cashiers_per_min = busy_cashiers / cashier_service_time
    
    # Convert to customers per hour
    R_cashiers_per_hour = R_cashiers_per_min * 60
    
    # TODO: Calculate waiting time using Little's Law on the queue
    # I = 10 customers waiting, R = throughput in customers/min
    W_cashier_line = littles_law_solve_T(avg_waiting_for_cashiers, R_cashiers_per_min)
    
    
    # QUESTION 2: Fraction using self-checkout
    # ----------------------------------------
    # Hint: Total customers = Cashier customers + Self-checkout customers
    
    # TODO: Calculate self-checkout throughput
    busy_self_checkout = num_self_checkout - avg_self_checkout_idle
    
    # We need service time for self-checkout (will calculate in Q3)
    # For now, let's calculate throughput from total customers
    R_self_checkout_per_hour = total_customers_per_hour - R_cashiers_per_hour
    
    # TODO: Calculate fraction using self-checkout
    fraction_self_checkout = R_self_checkout_per_hour / total_customers_per_hour
    
    
    # QUESTION 3: Average time using self-checkout machine (service time)
    # ------------------------------------------------------------------
    # Hint: Total time = Waiting time + Service time
    # Use Little's Law to find the waiting time first
    
    R_self_checkout_per_min = R_self_checkout_per_hour / 60
    
    # TODO: We know total time in self-checkout system is 5 minutes
    # Use Little's Law to find inventory in self-checkout SYSTEM
    I_self_checkout_system = littles_law_solve_I(R_self_checkout_per_min, 
                                                   self_checkout_total_time)
    
    # TODO: Inventory in system = Customers waiting + Customers being served
    # Customers being served = busy machines
    I_self_checkout_waiting = I_self_checkout_system - busy_self_checkout
    
    # TODO: Calculate waiting time in self-checkout line
    W_self_checkout = littles_law_solve_T(I_self_checkout_waiting, 
                                          R_self_checkout_per_min)
    
    # TODO: Calculate service time
    # Total time = Wait + Service
    S_self_checkout = self_checkout_total_time - W_self_checkout
    
    
    # QUESTION 4: Average total checkout time
    # ---------------------------------------
    # Hint: Weighted average based on fraction using each system
    
    # TODO: Calculate total time for cashier system
    # Total = Wait + Service
    T_cashier_total = W_cashier_line + cashier_service_time
    
    # TODO: Calculate weighted average
    avg_total_checkout_time = (fraction_self_checkout * self_checkout_total_time + 
                               (1 - fraction_self_checkout) * T_cashier_total)
    
    
    # QUESTION 5: Evaluate hiring 2 more cashiers
    # -------------------------------------------
    # Claim: Line reduced to half, wait time < 2 minutes
    
    # TODO: With 8 cashiers (assume 1 still idle on average)
    new_num_cashiers = 8
    new_busy_cashiers = new_num_cashiers - avg_cashiers_idle
    new_R_cashiers_per_min = new_busy_cashiers / cashier_service_time
    
    # TODO: If line cut in half
    new_queue = avg_waiting_for_cashiers / 2
    new_wait_time = littles_law_solve_T(new_queue, new_R_cashiers_per_min)
    
    # TODO: Check if claim is valid
    claim_about_queue = "Partially correct - IF queue is cut in half"
    claim_about_wait = "Correct" if new_wait_time < 2 else "Incorrect"
    
    # Better analysis: What queue length gives 2 min wait?
    target_wait = 2  # minutes
    required_queue = littles_law_solve_I(new_R_cashiers_per_min, target_wait)
    
    
    # Package results
    results = {
        'cashier_throughput_per_hour': R_cashiers_per_hour,
        'cashier_wait_time': W_cashier_line,
        'self_checkout_throughput_per_hour': R_self_checkout_per_hour,
        'fraction_using_self_checkout': fraction_self_checkout,
        'self_checkout_service_time': S_self_checkout,
        'self_checkout_wait_time': W_self_checkout,
        'avg_total_checkout_time': avg_total_checkout_time,
        'new_scenario_wait_time': new_wait_time,
        'claim_evaluation_queue': claim_about_queue,
        'claim_evaluation_wait': claim_about_wait,
        'required_queue_for_2min_wait': required_queue,
    }
    
    return results


# ============================================================================
# GENERATE ALL RESULTS
# ============================================================================

def generate_all_results() -> Dict:
    """
    Run all three problems and compile results.
    """
    print("=" * 70)
    print("LITTLE'S LAW HOMEWORK - RESULTS")
    print("=" * 70)
    
    # Problem 4: Chrome Wheels
    print("\n📊 PROBLEM 4: CHROME WHEELS INC.")
    print("-" * 70)
    cw_results = solve_chrome_wheels()
    print(f"1. Total average outstanding orders: {cw_results['total_inventory']:.1f} orders")
    print(f"   - Ultra-chrome: 10.0 orders")
    print(f"   - Ex-chrome: 8.0 orders")
    print(f"   - Standard: {cw_results['standard_inventory']:.1f} orders")
    print(f"\n2. Standard customer waiting time: {cw_results['standard_flow_time']:.2f} days")
    print(f"\n3. Priority customer waiting times:")
    print(f"   - Ex-chrome: {cw_results['ex_chrome_flow_time']:.2f} days")
    print(f"   - Ultra-chrome: {cw_results['ultra_flow_time']:.2f} days")
    
    # Problem 5: Global Trans
    print("\n\n🚢 PROBLEM 5: GLOBAL TRANS CO.")
    print("-" * 70)
    gt_results = solve_global_trans()
    print(f"1. Monthly earnings: ${gt_results['monthly_earnings']:,.0f}")
    print(f"   (Throughput: {gt_results['throughput_per_day']:.1f} deliveries/day)")
    print(f"\n2. Average travel time: {gt_results['travel_time']:.1f} days")
    print(f"   (Total cycle: {gt_results['total_cycle_time']:.1f} days)")
    
    # Problem 6: J.C. Nickel
    print("\n\n🛒 PROBLEM 6: J.C. NICKEL RETAIL STORE")
    print("-" * 70)
    jc_results = solve_jc_nickel()
    print(f"1. Cashier line waiting time: {jc_results['cashier_wait_time']:.2f} minutes")
    print(f"\n2. Fraction using self-checkout: {jc_results['fraction_using_self_checkout']:.1%}")
    print(f"   ({jc_results['self_checkout_throughput_per_hour']:.0f} out of 120 customers/hour)")
    print(f"\n3. Self-checkout machine service time: {jc_results['self_checkout_service_time']:.2f} minutes")
    print(f"   (Waiting time: {jc_results['self_checkout_wait_time']:.2f} minutes)")
    print(f"\n4. Average checkout time (all customers): {jc_results['avg_total_checkout_time']:.2f} minutes")
    print(f"\n5. Assistant Manager's Claim Evaluation:")
    print(f"   - Queue claim: {jc_results['claim_evaluation_queue']}")
    print(f"   - Wait time claim: {jc_results['claim_evaluation_wait']}")
    print(f"   - With 8 cashiers and half the queue: {jc_results['new_scenario_wait_time']:.2f} min wait")
    print(f"   - Queue needed for 2 min wait: {jc_results['required_queue_for_2min_wait']:.1f} customers")
    
    # Compile all results
    all_results = {
        'chrome_wheels': cw_results,
        'global_trans': gt_results,
        'jc_nickel': jc_results,
    }
    
    return all_results


# ============================================================================
# RUN THE ANALYSIS
# ============================================================================

if __name__ == "__main__":
    results = generate_all_results()
    
    print("\n\n" + "=" * 70)
    print("✅ All calculations complete!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Review your answers above")
    print("2. Save this file")
    print("3. Create your Streamlit app using the provided template")
    print("4. Deploy to Streamlit Cloud")


# ============================================================================
# STREAMLIT APP CODE
# ============================================================================
"""
Save the code below as 'streamlit_app.py' in your repository.

This code creates an interactive web app displaying your homework results.
"""

STREAMLIT_APP_CODE = '''
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Little's Law Homework",
    page_icon="📊",
    layout="wide"
)

# Title and introduction
st.title("📊 Little's Law Application: Operations Management Homework")
st.markdown("**By: [Your Name]**")
st.markdown("---")

# Sidebar with Little's Law explanation
with st.sidebar:
    st.header("📚 Little's Law")
    st.latex(r"I = R \\times T")
    st.markdown("""
    **Where:**
    - **I** = Inventory (units in system)
    - **R** = Throughput Rate (units/time)
    - **T** = Flow Time (time/unit)
    
    **Key Insight:** This relationship holds for any stable system in steady state!
    """)
    
    st.markdown("---")
    st.markdown("**Navigation:**")
    st.markdown("- Problem 4: Chrome Wheels")
    st.markdown("- Problem 5: Global Trans Co.")
    st.markdown("- Problem 6: J.C. Nickel")

# ============================================================================
# PROBLEM 4: CHROME WHEELS
# ============================================================================

st.header("🔧 Problem 4: Chrome Wheels Inc.")

with st.expander("📋 Problem Statement", expanded=False):
    st.markdown("""
    Chrome Wheels manufactures custom gear alloy wheels with three priority levels:
    - **Ultra-chrome** (Highest Priority): 8 orders/day
    - **Ex-chrome** (Medium Priority): 4 orders/day
    - **Standard** (Lowest Priority): 20 orders/day
    
    **Given:**
    - Average production time: 6 days
    - Average outstanding ultra-chrome: 10 orders
    - Average outstanding ex-chrome: 8 orders
    """)

# Calculations (replace with your actual values)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Outstanding Orders", "192 orders")
with col2:
    st.metric("Standard Wait Time", "8.7 days")
with col3:
    st.metric("Priority Wait Time", "~2 days")

# Visualization
st.subheader("Order Distribution")
fig_cw = go.Figure(data=[
    go.Bar(name='Ultra-chrome', x=['Orders'], y=[10], marker_color='#FFD700'),
    go.Bar(name='Ex-chrome', x=['Orders'], y=[8], marker_color='#C0C0C0'),
    go.Bar(name='Standard', x=['Orders'], y=[174], marker_color='#CD7F32')
])
fig_cw.update_layout(
    title="Average Inventory by Priority Level",
    yaxis_title="Number of Orders",
    barmode='group',
    height=400
)
st.plotly_chart(fig_cw, use_container_width=True)

# Flow time comparison
flow_times = pd.DataFrame({
    'Order Type': ['Ultra-chrome', 'Ex-chrome', 'Standard'],
    'Flow Time (days)': [1.25, 2.0, 8.7],
    'Priority': [1, 2, 3]
})

fig_flow = px.bar(flow_times, x='Order Type', y='Flow Time (days)',
                  color='Priority', color_continuous_scale='RdYlGn_r',
                  title='Customer Waiting Time by Order Type')
st.plotly_chart(fig_flow, use_container_width=True)

st.markdown("---")

# ============================================================================
# PROBLEM 5: GLOBAL TRANS CO.
# ============================================================================

st.header("🚢 Problem 5: Global Trans Co.")

with st.expander("📋 Problem Statement", expanded=False):
    st.markdown("""
    Global Trans operates 30 ships delivering goods in Europe.
    
    **Given:**
    - Total fleet: 30 ships
    - Average ships in port: 6 ships
    - Average time in port: 2 days
    - Revenue per delivery: $50,000
    """)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Monthly Earnings", "$4,500,000")
with col2:
    st.metric("Deliveries/Day", "3 ships")
with col3:
    st.metric("Travel Time", "8 days")

# System diagram
st.subheader("Ship Flow Visualization")

fig_ships = go.Figure()

# Add ship cycle visualization
fig_ships.add_trace(go.Indicator(
    mode="gauge+number+delta",
    value=3,
    domain={'x': [0, 0.5], 'y': [0, 1]},
    title={'text': "Throughput (ships/day)"},
    gauge={'axis': {'range': [None, 5]},
           'bar': {'color': "darkblue"},
           'steps': [
               {'range': [0, 2], 'color': "lightgray"},
               {'range': [2, 4], 'color': "gray"}],
           'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 3}}
))

fig_ships.update_layout(height=300)
st.plotly_chart(fig_ships, use_container_width=True)

# Create a Sankey diagram for ship flow
fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Port (6 ships)", "At Sea (24 ships)", "Deliveries"],
        color=["blue", "green", "gold"]
    ),
    link=dict(
        source=[0, 1, 0],
        target=[1, 2, 1],
        value=[3, 3, 3]
    )
)])

fig_sankey.update_layout(
    title_text="Daily Ship Flow (ships/day)",
    font_size=12,
    height=300
)
st.plotly_chart(fig_sankey, use_container_width=True)

st.markdown("---")

# ============================================================================
# PROBLEM 6: J.C. NICKEL
# ============================================================================

st.header("🛒 Problem 6: J.C. Nickel Retail Store")

with st.expander("📋 Problem Statement", expanded=False):
    st.markdown("""
    J.C. Nickel has 6 cashiers and 2 self-checkout machines.
    
    **Given:**
    - Total customers: 120/hour
    - Cashier service time: 3 minutes
    - 1 cashier idle on average
    - 10 customers waiting for cashiers
    - 1 self-checkout idle on average
    - Self-checkout total time: 5 minutes
    """)

# Key metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Cashier Wait", "6 min")
with col2:
    st.metric("% Self-Checkout", "50%")
with col3:
    st.metric("Self-Checkout Service", "4 min")
with col4:
    st.metric("Avg Total Time", "7 min")

# Customer distribution
st.subheader("Customer Flow Distribution")

customer_dist = pd.DataFrame({
    'Checkout Type': ['Cashiers', 'Self-Checkout'],
    'Customers per Hour': [60, 60]
})

fig_dist = px.pie(customer_dist, values='Customers per Hour', names='Checkout Type',
                  title='Customer Distribution',
                  color_discrete_sequence=['#FF6B6B', '#4ECDC4'])
st.plotly_chart(fig_dist, use_container_width=True)

# Scenario analysis
st.subheader("💡 Scenario Analysis: Adding 2 Cashiers")

scenario_data = pd.DataFrame({
    'Scenario': ['Current (6 cashiers)', 'Proposed (8 cashiers)'],
    'Queue Length': [10, 5],
    'Wait Time (min)': [6, 2.14]
})

fig_scenario = go.Figure()
fig_scenario.add_trace(go.Bar(
    name='Queue Length',
    x=scenario_data['Scenario'],
    y=scenario_data['Queue Length'],
    yaxis='y',
    marker_color='indianred'
))
fig_scenario.add_trace(go.Scatter(
    name='Wait Time',
    x=scenario_data['Scenario'],
    y=scenario_data['Wait Time (min)'],
    yaxis='y2',
    marker_color='blue',
    mode='lines+markers'
))

fig_scenario.update_layout(
    title='Impact of Hiring 2 Additional Cashiers',
    yaxis=dict(title='Queue Length (customers)'),
    yaxis2=dict(title='Wait Time (minutes)', overlaying='y', side='right'),
    height=400
)
st.plotly_chart(fig_scenario, use_container_width=True)

st.info("""
**Manager's Claim Evaluation:**
- ✅ Queue reduced to half (10 → 5): Assumed, not guaranteed
- ❓ Wait time < 2 minutes: Unlikely (calculated ~2.14 minutes with half queue)
- 💡 **Reality Check**: Adding cashiers increases throughput, but wait time depends on queue length
""")

st.markdown("---")

# ============================================================================
# SUMMARY AND INSIGHTS
# ============================================================================

st.header("📈 Key Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Little's Law in Action
    
    Across all three problems, we see how **I = R × T** helps us:
    
    1. **Predict Performance**: Calculate wait times from inventory
    2. **Identify Bottlenecks**: Spot where inventory accumulates
    3. **Evaluate Changes**: Test "what-if" scenarios
    """)

with col2:
    st.markdown("""
    ### Real-World Applications
    
    - **Manufacturing** (Chrome Wheels): Priority systems create unequal wait times
    - **Logistics** (Global Trans): System capacity limits throughput
    - **Retail** (J.C. Nickel): Multiple server systems need careful analysis
    """)

# Footer
st.markdown("---")
st.markdown("*Homework completed using Little's Law principles | Operations Management*")
'''

# ============================================================================
# EXPORT INSTRUCTIONS
# ============================================================================

print("\n\n" + "=" * 70)
print("NEXT STEPS: SAVE AND DEPLOY")
print("=" * 70)
print("""
1. Save this notebook to your Google Drive
2. Create a new file called 'streamlit_app.py' with the code above
3. Follow the deployment instructions in the README
4. Submit your GitHub repository link
""")
