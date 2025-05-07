
import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
# st.set_page_config(
#     page_title="Streamlit デモ",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ============================================
# タイトルと説明
# ============================================
st.title("Streamlit 初心者向けデモ")
st.markdown("### コメントを解除しながらStreamlitの機能を学びましょう")
st.markdown("このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。")

# ============================================
# サイドバー 
# ============================================
st.sidebar.header("デモのガイド")
st.sidebar.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。")

# ============================================
# 基本的なUI要素
# ============================================
st.header("基本的なUI要素")
st.subheader("テキスト入力")
name = st.text_input("あなたの名前", "ゲスト")
st.write(f"こんにちは、{name}さん！")

st.subheader("スライダー")
age = st.slider("年齢", 0, 100, 25)
st.write(f"あなたの年齢: {age}")

st.subheader("カラムレイアウト")
col1, col2 = st.columns(2)
with col1:
    st.write("これは左カラムです")
    st.number_input("数値を入力", value=10)
with col2:
    st.write("これは右カラムです")
    st.metric("メトリクス", "42", "2%")

# 電卓
st.subheader("電卓")
a = st.number_input("数字Aを入力", value=0)
b = st.number_input("数字Bを入力", value=0)
operation = st.selectbox("演算子を選んでください", ["＋", "−", "×", "÷"])

if st.button("計算する"):
    if operation == "＋":
        st.write(f"結果: {a + b}")
    elif operation == "−":
        st.write(f"結果: {a - b}")
    elif operation == "×":
        st.write(f"結果: {a * b}")
    elif operation == "÷":
        st.write("結果: {:.2f}".format(a / b) if b != 0 else "error: 0で割れません")

# ToDoリスト
st.subheader("ToDoリスト（シンプル版）")
if "todos" not in st.session_state:
    st.session_state.todos = []

task = st.text_input("やることを入力", key="new_task")
if st.button("追加"):
    if task:
        st.session_state.todos.append({"text": task, "done": False})
        st.session_state.new_task = ""  
        st.experimental_rerun()

for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([6, 2])
    label = f"[完了] {todo['text']}" if todo["done"] else todo["text"]
    with col1:
        st.write(label)
    with col2:
        if not todo["done"]:
            if st.button("完了", key=f"done_{i}"):
                st.session_state.todos[i]["done"] = True
                st.experimental_rerun()
        else:
            if st.button("削除", key=f"del_{i}"):
                st.session_state.todos.pop(i)
                st.experimental_rerun()
                break

st.divider()
st.subheader("このデモの使い方")
st.markdown("""
1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
2. 確認したい機能のコメントを解除します（先頭の#を削除）
3. 変更を保存して、ブラウザで結果を確認します
4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
""")

st.code("""
# コメントアウトされた例:
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")

# コメントを解除した例:
if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")
""")
